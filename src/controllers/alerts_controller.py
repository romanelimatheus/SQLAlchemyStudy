"""Alerts controller."""

from dataclasses import dataclass

from sqlalchemy import Engine


@dataclass
class AlertController:
    """Alerts controller."""

    engine: Engine

    def get_frames_alerts(self: "AlertController") -> None:
        """Return frames with alerts."""
