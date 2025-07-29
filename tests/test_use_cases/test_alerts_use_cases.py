import pytest
from sqlalchemy import Engine

from src.use_cases.alerts_use_cases.integrity_alerts_use_case import IntegrityAlertsUseCase
from tests import engine
from tests.mocks.goose_frame_mock import generate_goose_frame
from tests.mocks.integrity_alert_mock import generate_integrity_alert


@pytest.fixture
def engine_mock() -> Engine:
    return engine()

class TestIntegrityAlertUseCase:
    def test_one_frame_without_integrity_alert(self, engine_mock: Engine) -> None:
        generate_goose_frame(engine=engine_mock)
        results = IntegrityAlertsUseCase().exec(engine_mock)
        goose, alert = results[0]._tuple()  # noqa: SLF001

        if goose is None:
            msg = "Should return one frame, but returned None"
            raise AssertionError(msg)
        if alert is not None:
            msg = "Should return no integrity alert, but returned: %s"
            raise AssertionError(msg % alert)

    def test_one_frame_with_integrity_alert_error(self, engine_mock: Engine) -> None:
        generate_integrity_alert(engine=engine_mock)
        results = IntegrityAlertsUseCase().exec(engine_mock)
        goose, alert = results[0]._tuple()  # noqa: SLF001

        if goose is None:
            msg = "Should return one frame, but returned None"
            raise AssertionError(msg)
        if alert is None:
            msg = "Should return integrity alert, but returned: %s"
            raise AssertionError(msg % alert)

    def test_one_frame_with_integrity_alert_fixed(self, engine_mock: Engine) -> None:
        generate_integrity_alert(engine=engine_mock, with_fixed=True)
        results = IntegrityAlertsUseCase().exec(engine_mock)
        goose, alert = results[0]._tuple()  # noqa: SLF001

        if len(results) != 1:
            msg = "Should return one frame, but returned %s"
            raise AssertionError(msg % len(results))
        if goose is None:
            msg = "Should return one frame, but returned None"
            raise AssertionError(msg)
        if alert is None:
            msg = "Should return integrity alert, but returned: %s"
            raise AssertionError(msg % alert)
        if alert.error:
            msg = "Should return integrity alert fixed, but returned: %s"
            raise AssertionError(msg % alert)

    def test_two_frames_without_integrity_alert(self, engine_mock: Engine) -> None:
        generate_goose_frame(engine=engine_mock)
        generate_goose_frame(engine=engine_mock)

        results = IntegrityAlertsUseCase().exec(engine_mock)
        for result in results:
            goose, alert = result._tuple()  # noqa: SLF001

            if goose is None:
                msg = "Should return one frame, but returned None"
                raise AssertionError(msg)
            if alert is not None:
                msg = "Should return no integrity alert, but returned: %s"
                raise AssertionError(msg % alert)
        if len(results) != 2:
            msg = "Should return two frames, but returned %s"
            raise AssertionError(msg % len(results))

    def test_two_frames_with_integrity_alert_error(self, engine_mock: Engine) -> None:
        generate_integrity_alert(engine=engine_mock)
        generate_integrity_alert(engine=engine_mock)
        results = IntegrityAlertsUseCase().exec(engine_mock)
        for result in results:
            goose, alert = result._tuple()  # noqa: SLF001

            if goose is None:
                msg = "Should return one frame, but returned None"
                raise AssertionError(msg)
            if alert is None:
                msg = "Should return integrity alert, but returned: %s"
                raise AssertionError(msg % alert)
        if len(results) != 2:
            msg = "Should return two frames, but returned %s"
            raise AssertionError(msg % len(results))

    def test_two_frames_with_integrity_alert_fixed(self, engine_mock: Engine) -> None:
        generate_integrity_alert(engine=engine_mock, with_fixed=True)
        generate_integrity_alert(engine=engine_mock, with_fixed=True)
        results = IntegrityAlertsUseCase().exec(engine_mock)
        for result in results:
            goose, alert = result._tuple()  # noqa: SLF001

            if goose is None:
                msg = "Should return one frame, but returned None"
                raise AssertionError(msg)
            if alert is None:
                msg = "Should return integrity alert, but returned: %s"
                raise AssertionError(msg % alert)
            if alert.error:
                msg = "Should return integrity alert fixed, but returned: %s"
                raise AssertionError(msg % alert)
        if len(results) != 2:
            msg = "Should return two frames, but returned %s"
            raise AssertionError(msg % len(results))
