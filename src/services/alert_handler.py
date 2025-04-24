"""Handler to save alerts."""
from dataclasses import dataclass, field
from threading import Event

from sqlalchemy import Engine
from sqlalchemy.orm import Session

from src.models.alerts import Alerts, AlertsLobby


@dataclass
class AlertHandler:
    """Handler to save alerts."""

    engine: Engine
    _queue: list[Alerts] = field(default_factory=list)
    _queue_event: Event = field(default_factory=Event)

    def add(self: "AlertHandler", alert: Alerts) -> None:
        """Add alert to be commited on DB."""
        self._queue.append(alert)
        self._queue_event.set()

    def alert_bus(self: "AlertHandler") -> None:
        """Alert bus."""
        alert = self._queue.pop(0)
        alert_hook = AlertsLobby.from_alert(alert)
        with Session(self.engine) as session:
            session.add(alert)
            session.add(alert_hook)
            session.commit()

    def process(self: "AlertHandler") -> None:
        """Alert bus loop to save alerts on DB."""
        while self._queue_event.wait():
            self.alert_bus()
            if self._queue == []:
                self._queue_event.clear()
