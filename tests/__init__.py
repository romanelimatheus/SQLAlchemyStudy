from sqlalchemy import Engine


def engine() -> Engine:
    from sqlalchemy import create_engine

    from src.models.base import Base
    engine = create_engine("sqlite:///test.db")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return engine
