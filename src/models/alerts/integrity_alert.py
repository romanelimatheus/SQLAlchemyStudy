"""Integrity alert models."""
import enum
from uuid import UUID

from sqlalchemy import Boolean, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class FieldsEnum(enum.Enum):
    """Goose Integrity Alert Field Enum."""

    GOOSE_ID = 1
    GOCBREF = 2

class GooseIntegrityAlert(Base):
    """Goose Integrity Alert Model."""

    __tablename__ = "goose_integrity_alert"

    goose_frame_id: Mapped[UUID] = mapped_column(ForeignKey("goose_frame.id"))
    field: Mapped[FieldsEnum] = mapped_column(Enum(FieldsEnum))
    error: Mapped[bool] = mapped_column(Boolean)
    value: Mapped[str] = mapped_column(String)
