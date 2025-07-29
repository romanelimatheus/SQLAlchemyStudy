import pytest
from sqlalchemy import Engine

from src.controllers.alerts_controller import AlertController
from tests import engine
from tests.mocks.integrity_alert_mock import generate_integrity_alert


@pytest.fixture
def engine_mock() -> Engine:
    return engine()

class TestAlertsController:

    def test_frame_with_integrity_alert(self, engine_mock: Engine) -> None:
        generate_integrity_alert(engine=engine_mock)
        frame_alerts = AlertController(engine=engine_mock).get_frames_alerts()
        if len(frame_alerts) != 1:
            msg = "Should return no frames, but returned: %s"
            raise AssertionError(msg % len(frame_alerts))

    def test_frame_with_fixed_integrity_alert(self, engine_mock: Engine) -> None:
        generate_integrity_alert(engine=engine_mock, with_fixed=True)
        frame_alerts = AlertController(engine=engine_mock).get_frames_alerts()
        if len(frame_alerts) != 1:
            msg = "Should return no frames, but returned: %s"
            raise AssertionError(msg % len(frame_alerts))

    def test_frame_with_no_integrity_alert(self, engine_mock: Engine) -> None:
        frame_alerts = AlertController(engine=engine_mock).get_frames_alerts()
        if len(frame_alerts) != 0:
            msg = "Should return no frames, but returned: %s"
            raise AssertionError(msg % len(frame_alerts))
