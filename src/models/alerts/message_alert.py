"""Integrity alert models."""
from uuid import UUID

from sqlalchemy import Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class GooseMessageAlert(Base):
    """Goose Integrity Alert Model."""

    __tablename__ = "goose_message_alert"

    abscense: Mapped[bool] = mapped_column(Boolean)
    goose_frame_id: Mapped[UUID] = mapped_column(ForeignKey("goose_frame.id"))

    @classmethod
    def build(cls: type["GooseMessageAlert"],
        goose_frame_id: UUID|None=None, *, abscense: bool=True,
    ) -> "GooseMessageAlert":
        """Class instance used for tests."""
        if goose_frame_id is None:
            goose_frame_id = UUID("00000000-0000-0000-0000-000000000000")
        return cls(goose_frame_id=goose_frame_id, abscense=abscense)
