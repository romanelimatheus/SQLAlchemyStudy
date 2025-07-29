"""Access infos based on integrity alert."""

from sqlalchemy import Select, select
from sqlalchemy.orm import aliased

from src.models.alerts.integrity_alert import GooseIntegrityAlert


class IntegrityAlertContext:
    """Context based on integrity alert."""

    def get_last_integrity_alerts(self: "IntegrityAlertContext") -> Select[tuple[GooseIntegrityAlert]]:
        """Get integrity alerts."""
        last_alerts = aliased(GooseIntegrityAlert, name="last")
        return select(last_alerts).group_by(last_alerts.goose_frame_id).order_by(last_alerts.created_at.desc())
