from threading import Thread

import pytest
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from src.models.alerts.integrity_alert import GooseIntegrityAlert
from src.services.alert_handler import AlertHandler
from tests import engine


@pytest.fixture
def engine_mock() -> Engine:
    return engine()

class TestAlertHandler:

    def test_add(self, engine_mock: Engine) -> None:
        alert_handler = AlertHandler(engine=engine_mock)
        integrity_alert = GooseIntegrityAlert.build()
        alert_handler.add(integrity_alert)
        assert alert_handler.queue_fill.is_set()
        assert alert_handler.queue[-1] == integrity_alert

    def test_alert_bus(self, engine_mock: Engine) -> None:
        alert_handler = AlertHandler(engine=engine_mock)
        integrity_alert = GooseIntegrityAlert.build()
        alert_handler.alert_bus(integrity_alert)

        with Session(engine_mock) as session:
            integrity_alert_db = session.get(GooseIntegrityAlert, integrity_alert.id)
            assert integrity_alert_db is not None

    def test_process(self: "TestAlertHandler", engine_mock: Engine) -> None:
        alert_handler = AlertHandler(engine=engine_mock)
        integrity_alert = GooseIntegrityAlert.build()
        alert_handler.add(integrity_alert)
        thread = Thread(target=alert_handler.process, daemon=True)
        thread.start()

        alert_handler.queue_free.wait(1)
        assert alert_handler.queue == []
        assert not alert_handler.queue_fill.is_set()
