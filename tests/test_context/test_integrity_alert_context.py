import pytest
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from src.context.integrity_alert_context import IntegrityAlertContext
from tests import engine
from tests.mocks.integrity_alert_mock import generate_integrity_alert


@pytest.fixture
def engine_mock() -> Engine:
    return engine()

class TestIntegrityAlertContext:
    def test_last_alert_does_not_exist(self, engine_mock: Engine) -> None:
        select = IntegrityAlertContext().get_last_integrity_alerts()
        with Session(engine_mock) as session:
            result = session.execute(select).all()

        if result is None or len(result) != 0:
            msg = "Should return zero registers"
            raise AssertionError(msg)

    def test_last_alert_exists(self, engine_mock: Engine) -> None:
        generate_integrity_alert(engine=engine_mock)
        select = IntegrityAlertContext().get_last_integrity_alerts()
        with Session(engine_mock) as session:
            result = session.execute(select).all()

        if result is None or len(result) != 1:
            msg = "Should return one register"
            raise AssertionError(msg)

    def test_last_alert_more_than_one(self, engine_mock: Engine) -> None:
        generate_integrity_alert(engine=engine_mock, with_fixed=True)
        select = IntegrityAlertContext().get_last_integrity_alerts()
        with Session(engine_mock) as session:
            result = session.execute(select).scalars().all()

        if result is None or len(result) != 1:
            msg = "Should return one register, but returns %s: %s"
            raise AssertionError(msg %(len(result), result))
        if result[0].error:
            msg = "Should return one integrity alert fixed, but returns: %s"
            raise AssertionError(msg % result[0])

    def test_last_alert_more_than_one_for_two_frames(self, engine_mock: Engine) -> None:
        generate_integrity_alert(engine=engine_mock, with_fixed=True)
        generate_integrity_alert(engine=engine_mock, with_fixed=True)
        select = IntegrityAlertContext().get_last_integrity_alerts()
        with Session(engine_mock) as session:
            result = session.execute(select).scalars().all()

        if result is None or len(result) != 2:
            msg = "Should return one register, but returns %s: %s"
            raise AssertionError(msg %(len(result), result))
        if result[0].error:
            msg = "Should return one integrity alert fixed, but returns: %s"
            raise AssertionError(msg % result[0])
        if result[1].error:
            msg = "Should return one integrity alert fixed, but returns: %s"
            raise AssertionError(msg % result[1])
