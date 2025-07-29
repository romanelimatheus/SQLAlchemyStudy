import pytest
from sqlalchemy import Engine, StaticPool, create_engine

from src.models.base import Base


def engine() -> Engine:
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread":False}, poolclass=StaticPool)
    Base.metadata.create_all(engine)
    return engine
