"""IED Model."""

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src import Base

if TYPE_CHECKING:
    from src.models import GooseFrame


class IED(Base):
    """IED Model."""

    __tablename__ = "ied"

    ip : Mapped[str] = mapped_column(String)
    name : Mapped[str] = mapped_column(String)
    vendor : Mapped[str] = mapped_column(String)
    goose_frames : Mapped[list["GooseFrame"]] = relationship(back_populates="ied", default_factory=list)
