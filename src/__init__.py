"""Initialize configurations."""

from uuid import UUID, uuid4

from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column


class Base(MappedAsDataclass, DeclarativeBase, kw_only=True):
    """Base model class."""

    id: Mapped[UUID] = mapped_column(primary_key=True, default_factory=uuid4)
