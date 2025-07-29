"""Alerts Lobby model."""
import enum
from uuid import UUID

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.models.alerts.integrity_alert import GooseIntegrityAlert
from src.models.alerts.message_alert import GooseMessageAlert
from src.models.base import Base

type Alerts = GooseIntegrityAlert | GooseMessageAlert

class AlertsEnum(enum.IntEnum):
    """Alerts Enum."""

    INTEGRITY = 1
    MESSAGE = 2

    @classmethod
    def from_instance(cls: type["AlertsEnum"], alert: Alerts) -> "AlertsEnum":
        """Create alert enum from alert instance."""
        if isinstance(alert, GooseIntegrityAlert):
            return AlertsEnum.INTEGRITY
        if isinstance(alert, GooseMessageAlert):
            return AlertsEnum.MESSAGE
        msg = f"Unknown alert type: {type(alert)}"
        raise ValueError(msg)

class AlertsLobby(Base):
    """Alerts Lobby model."""

    __tablename__ = "alerts_lobby"
    alert_reference: Mapped[AlertsEnum] = mapped_column(Enum(AlertsEnum))
    alert_id: Mapped[UUID]

    @classmethod
    def from_alert(cls: type["AlertsLobby"], alert: Alerts) -> "AlertsLobby":
        """Create alert lobby from alert."""
        reference_enum = AlertsEnum.from_instance(alert)
        return cls(alert_reference=reference_enum, alert_id=alert.id)
