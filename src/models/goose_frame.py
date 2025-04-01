"""GooseFrame model."""
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src import Base

if TYPE_CHECKING:
    from src.models.ied import IED


class GooseFrame(Base):
    """GooseFrame model."""

    __tablename__ = "goose_frame"

    goose_id: Mapped[str] = mapped_column(String)
    gocb_ref: Mapped[str] = mapped_column(String)
    ied_src_id: Mapped[UUID] = mapped_column(ForeignKey("ied.id"))
    ied_dst_id: Mapped[UUID] = mapped_column(ForeignKey("ied.id"))

    ied_src: Mapped["IED"] = relationship(foreign_keys=[ied_src_id], back_populates="goose_frames_publications")
    ied_dst: Mapped["IED"] = relationship(foreign_keys=[ied_dst_id], back_populates="goose_frames_subscriptions")
