"""Integrity alerts use case."""

from sqlalchemy import Engine, select
from sqlalchemy.orm import Session

from src.context.goose_frame_context import GooseFrameContext
from src.context.integrity_alert_context import IntegrityAlertContext


class IntegrityAlertsUseCase:
    """Integrity alerts use case."""

    def exec(self: "IntegrityAlertsUseCase", engine: Engine) -> None:
        goose_frame_context = GooseFrameContext()
        integrity_alert_context = IntegrityAlertContext()

        goose_frames = goose_frame_context.get_goose_frames().subquery()
        integrity_alerts = integrity_alert_context.get_valid_integrity_alerts().subquery()
        result = select(
            goose_frames,
            integrity_alerts,
        )
        with Session(engine) as session:
            return session.execute(result).all()
