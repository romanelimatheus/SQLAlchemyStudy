from sqlalchemy import Engine, create_engine

from src.models.base import Base


def engine() -> Engine:
    engine = create_engine("sqlite:///test.db")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return engine
