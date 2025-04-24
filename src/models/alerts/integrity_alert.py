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

    @classmethod
    def default(cls: type["GooseIntegrityAlert"]) -> "GooseIntegrityAlert":
        """Class instance used for tests."""
        return cls(
            goose_frame_id=UUID("f067fc5c-2497-4fea-a177-d994214c69bb"),
            field = FieldsEnum.GOOSE_ID,
            error = True,
            value = "test",
        )
