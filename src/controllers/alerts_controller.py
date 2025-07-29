"""Alerts controller."""

from collections.abc import Sequence
from dataclasses import dataclass

from sqlalchemy import Engine, Row

from src.models.alerts.integrity_alert import GooseIntegrityAlert
from src.models.goose_frame import GooseFrame
from src.use_cases.alerts_use_cases.integrity_alerts_use_case import IntegrityAlertsUseCase


@dataclass
class AlertController:
    """Alerts controller."""

    engine: Engine

    def get_frames_alerts(self: "AlertController") -> Sequence[Row[tuple[GooseFrame, GooseIntegrityAlert]]]:
        """Return frames with alerts."""
        return IntegrityAlertsUseCase().exec(self.engine)
