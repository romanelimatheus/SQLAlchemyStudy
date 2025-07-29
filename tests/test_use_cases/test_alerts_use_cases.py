import pytest
from sqlalchemy import Engine

from src.use_cases.alerts_use_cases.integrity_alerts_use_case import IntegrityAlertsUseCase
from tests import engine
from tests.mocks.goose_frame_mock import generate_goose_frame


@pytest.fixture
def engine_mock() -> Engine:
    return engine()

class TestIntegrityAlertUseCase:
    def test_one_frame_without_integrity_alert(self, engine_mock: Engine) -> None:
        generate_goose_frame(engine=engine_mock)
        result = IntegrityAlertsUseCase().exec(engine_mock)
        print(result[0].tuple())
        goose, alert = result[0]
        if goose is None:
            msg = "Should return one frame, but returned None"
            raise AssertionError(msg)
        if alert is not None:
            msg = "Should return no integrity alert, but returned: %s"
            raise AssertionError(msg % alert)

    def test_one_frame_with_integrity_alert_error(self, engine_mock: Engine) -> None:
        pass

    def test_one_frame_with_integrity_alert_fixed(self, engine_mock: Engine) -> None:
        pass

    def test_two_frames_without_integrity_alert(self, engine_mock: Engine) -> None:
        pass

    def test_two_frames_with_integrity_alert_error(self, engine_mock: Engine) -> None:
        pass

    def test_two_frames_with_integrity_alert_fixed(self, engine_mock: Engine) -> None:
        pass
