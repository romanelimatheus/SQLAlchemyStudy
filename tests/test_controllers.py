import pytest
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from src.controllers.alerts_controller import AlertController
from src.models.alerts.integrity_alert import GooseIntegrityAlert
from src.models.goose_frame import GooseFrame
from src.models.ied import IED
from tests import engine


@pytest.fixture
def engine_mock() -> Engine:
    return engine()

class TestAlertsController:

    def generate_integrity_alert(self: "TestAlertsController", engine: Engine, *, with_fixed: bool = False) -> None:
        with Session(engine) as session:
            ied_src = IED.build(name="src")
            ied_dst = IED.build(name="dst")
            goose_frame = GooseFrame.build(ied_src=ied_src, ied_dst=ied_dst)
            session.add(ied_src)
            session.add(ied_dst)
            session.add(goose_frame)
            session.add(GooseIntegrityAlert.build(goose_frame_id=goose_frame.id))
            if with_fixed:
                integrity_alert_fix = GooseIntegrityAlert.build(
                    goose_frame_id=goose_frame.id, value="Test", error=False,
                )
                session.add(integrity_alert_fix)
            session.commit()

    def test_frame_with_integrity_alert(self, engine_mock: Engine) -> None:
        self.generate_integrity_alert(engine=engine_mock)
        frame_alerts = AlertController(engine=engine_mock).get_frames_alerts()
        print(frame_alerts)
        assert False

    # def test_frame_with_fixed_integrity_alert(self, engine_mock: Engine) -> None:
    #     engine_mock = engine()
    #     self.generate_integrity_alert(engine=engine_mock, with_fixed=True)
    #     frame_alerts = AlertController(engine=engine_mock).get_frames_alerts()

    # def test_frame_with_no_integrity_alert(self, engine_mock: Engine) -> None:
    #     engine_mock = engine()
    #     frame_alerts = AlertController(engine=engine_mock).get_frames_alerts()
