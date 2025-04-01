"""Main module to run database."""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src import Base
from src.models.goose_frame import GooseFrame
from src.models.ied import IED


def main() -> None:
    """."""
    engine = create_engine("sqlite:///database.db", echo=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        ied = IED(
            ip="127.0.0.1",
            name="test",
            vendor="test",
        )
        goose_frame = GooseFrame(
            goose_id="test",
            gocb_ref="test",
            ied_id=ied.id,
            ied=ied,
        )

        session.add(ied)
        session.add(goose_frame)
        session.commit()



if __name__ == "__main__":
    main()
