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
        ied_src = IED(
            ip="127.0.0.1",
            name="Origem",
            vendor="test",
        )
        ied_dst = IED(
            ip="127.0.0.1",
            name="Destino",
            vendor="test",
        )
        goose_frame = GooseFrame(
            goose_id="test",
            gocb_ref="test",
            ied_src_id=ied_src.id,
            ied_dst_id=ied_dst.id,
            ied_src=ied_src,
            ied_dst=ied_dst,
        )

        session.add(ied_src)
        session.add(ied_dst)
        session.add(goose_frame)
        session.commit()



if __name__ == "__main__":
    main()
