"""IED Model."""
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import GooseFrame
from src.models.base import Base


class IED(Base):
    """IED Model."""

    __tablename__ = "ied"

    ip : Mapped[str] = mapped_column(String)
    name : Mapped[str] = mapped_column(String)
    vendor : Mapped[str] = mapped_column(String)
    goose_frames_publications : Mapped[list["GooseFrame"]] = relationship(GooseFrame,
        foreign_keys=[GooseFrame.ied_src_id], back_populates="ied_src", default_factory=list)
    goose_frames_subscriptions : Mapped[list["GooseFrame"]] = relationship(GooseFrame,
        foreign_keys=[GooseFrame.ied_dst_id], back_populates="ied_dst", default_factory=list)
