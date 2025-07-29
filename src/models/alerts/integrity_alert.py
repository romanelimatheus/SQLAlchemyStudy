"""Integrity alert models."""
import enum
from uuid import UUID

from sqlalchemy import Boolean, DateTime, Enum, ForeignKey, String, func
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
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())

    @classmethod
    def build(cls: type["GooseIntegrityAlert"],
        goose_frame_id: UUID|None=None, field: FieldsEnum=FieldsEnum.GOOSE_ID, value: str="Test", *, error: bool=True,
    ) -> "GooseIntegrityAlert":
        """Class instance used for tests."""
        if goose_frame_id is None:
            goose_frame_id = UUID("00000000-0000-0000-0000-000000000000")
        return cls(
            goose_frame_id=goose_frame_id,
            field = field,
            error = error,
            value = value,
        )
