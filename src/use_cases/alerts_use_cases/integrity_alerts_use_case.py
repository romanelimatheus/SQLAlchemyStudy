"""Integrity alerts use case."""

from sqlalchemy import Engine, select
from sqlalchemy.engine import TupleResult
from sqlalchemy.orm import aliased

from src.context.integrity_alert_context import IntegrityAlertContext
from src.models.alerts.integrity_alert import GooseIntegrityAlert
from src.models.goose_frame import GooseFrame

type IntegrityAlertResponse = TupleResult[tuple[GooseFrame, GooseIntegrityAlert]]

class IntegrityAlertsUseCase:
    """Integrity alerts use case."""

    def exec(self: "IntegrityAlertsUseCase", engine: Engine) -> IntegrityAlertResponse:
        """Get integrity alerts for each frame."""
        integrity_alert_context = IntegrityAlertContext()

        integrity_alerts = integrity_alert_context.get_valid_integrity_alerts().subquery()
        integrity_alert = aliased(GooseIntegrityAlert, integrity_alerts)
        query = select(
            GooseFrame,
            integrity_alert,
        ).join(
            integrity_alerts,
            GooseFrame.id == integrity_alert.goose_frame_id,
        ).order_by(
            GooseFrame.id,
        )
        with engine.connect() as connection:
            return connection.execute(query).tuples()
