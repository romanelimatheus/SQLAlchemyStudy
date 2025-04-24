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
    def default(cls: type["GooseMessageAlert"]) -> "GooseMessageAlert":
        """Class instance used for tests."""
        return GooseMessageAlert(goose_frame_id=UUID("f067fc5c-2497-4fea-a177-d994214c69bb"),abscense=False)
