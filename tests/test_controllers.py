from uuid import uuid4

import pytest
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from src.controllers.alerts_controller import AlertController
from src.models.alerts.integrity_alert import GooseIntegrityAlert
from tests import engine


@pytest.fixture
def engine_mock() -> Engine:
    return engine()

class TestAlertsController:

    def generate_integrity_alert(self: "TestAlertsController", engine: Engine, *, with_fixed: bool = False) -> None:
        with Session(engine) as session:
            session.add(GooseIntegrityAlert.default())
            if with_fixed:
                integrity_alert_fix = GooseIntegrityAlert.default()
                integrity_alert_fix.error = False
                integrity_alert_fix.id = uuid4()
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
