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
    _queue_fill: Event = field(default_factory=Event)
    _queue_free: Event = field(default_factory=Event)

    @property
    def queue(self: "AlertHandler") -> list[Alerts]:
        """Get queue."""
        return self._queue

    @property
    def queue_fill(self: "AlertHandler") -> Event:
        """Get queue fill event."""
        return self._queue_fill

    @property
    def queue_free(self: "AlertHandler") -> Event:
        """Get queue free event."""
        return self._queue_free

    def add(self: "AlertHandler", alert: Alerts) -> None:
        """Add alert to be commited on DB."""
        self._queue.append(alert)
        self._queue_fill.set()
        self._queue_free.clear()

    def alert_bus(self: "AlertHandler", alert: Alerts) -> None:
        """Alert bus."""
        alert_hook = AlertsLobby.from_alert(alert)
        with Session(self.engine, expire_on_commit=False) as session:
            session.add(alert)
            session.add(alert_hook)
            session.commit()

    def process(self: "AlertHandler") -> None:
        """Alert bus loop to save alerts on DB."""
        while self._queue_fill.wait():
            alert = self._queue.pop(0)
            self.alert_bus(alert)
            if self._queue == []:
                self._queue_fill.clear()
                self._queue_free.set()
