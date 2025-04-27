"""Integrity alerts use case."""

from collections.abc import Sequence

from sqlalchemy import Engine, Row, select
from sqlalchemy.orm import Session, aliased

from src.context.integrity_alert_context import IntegrityAlertContext
from src.models.alerts.integrity_alert import GooseIntegrityAlert
from src.models.goose_frame import GooseFrame

type IntegrityAlertResponse = Sequence[Row[tuple[GooseFrame, GooseIntegrityAlert]]]

class IntegrityAlertsUseCase:
    """Integrity alerts use case."""

    def exec(self: "IntegrityAlertsUseCase", engine: Engine) -> IntegrityAlertResponse:
        """Get integrity alerts for each frame."""
        integrity_alert_context = IntegrityAlertContext()

        integrity_alerts = integrity_alert_context.get_valid_integrity_alerts().subquery()
        integrity_alert = aliased(GooseIntegrityAlert, integrity_alerts)
        result = select(
            GooseFrame,
            integrity_alert,
        ).join(
            integrity_alerts,
            GooseFrame.id == integrity_alert.goose_frame_id,
        ).order_by(
            GooseFrame.id,
        )
        with Session(engine) as session:
            return session.execute(result).all()
