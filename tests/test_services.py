from threading import Thread
from time import sleep

import pytest
from sqlalchemy import Engine

from src.models.alerts.integrity_alert import GooseIntegrityAlert
from src.services.alert_handler import AlertHandler
from tests import engine


@pytest.fixture(scope="session", autouse=True)
def engine_mock() -> Engine:
    return engine()

class TestAlertHandler:

    def test_add(self, engine_mock: Engine) -> None:
        alert_handler = AlertHandler(engine=engine_mock)
        integrity_alert = GooseIntegrityAlert.build()
        alert_handler.add(integrity_alert)
        assert alert_handler.queue_event.is_set()
        assert alert_handler.queue[-1] == integrity_alert

    def test_alert_bus(self) -> None:
        assert True

    def test_process(self: "TestAlertHandler", engine_mock: Engine) -> None:
        alert_handler = AlertHandler(engine=engine_mock)
        integrity_alert = GooseIntegrityAlert.build()
        alert_handler.add(integrity_alert)
        thread = Thread(target=alert_handler.process, daemon=True)
        thread.start()

        sleep(0.1)

        assert alert_handler.queue == []
        assert not alert_handler.queue_event.is_set()
