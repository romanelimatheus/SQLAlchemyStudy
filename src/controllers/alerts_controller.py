"""Alerts controller."""

from dataclasses import dataclass

from sqlalchemy import Engine

from src.use_cases.alerts_use_cases.integrity_alerts_use_case import IntegrityAlertResponse, IntegrityAlertsUseCase


@dataclass
class AlertController:
    """Alerts controller."""

    engine: Engine

    def get_frames_alerts(self: "AlertController") -> IntegrityAlertResponse:
        """Return frames with alerts."""
        return IntegrityAlertsUseCase().exec(self.engine)
