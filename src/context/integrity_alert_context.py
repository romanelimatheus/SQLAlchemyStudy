"""Access infos based on integrity alert."""

from sqlalchemy import Select, select
from sqlalchemy.orm import aliased

from models.alerts.integrity_alert import GooseIntegrityAlert


class IntegrityAlertContext:
    """Context based on integrity alert."""

    def get_valid_integrity_alerts(self: "IntegrityAlertContext") -> Select[tuple[GooseIntegrityAlert]]:
        """Get integrity alerts."""
        valid_alerts = aliased(GooseIntegrityAlert, name="errors")
        invalid_alerts = aliased(GooseIntegrityAlert, name="fixed")
        return select(
            valid_alerts,
        ).join(
            invalid_alerts, valid_alerts.goose_frame_id == invalid_alerts.goose_frame_id, isouter=True,
        ).where(
            valid_alerts.error.is_(True),
        )
