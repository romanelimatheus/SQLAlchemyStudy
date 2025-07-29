from sqlalchemy import Engine
from sqlalchemy.orm import Session

from src.models.goose_frame import GooseFrame
from src.models.ied import IED


def generate_goose_frame(engine: Engine) -> None:
    with Session(engine) as session:
        ied_src = IED.build(name="src")
        ied_dst = IED.build(name="dst")
        goose_frame = GooseFrame.build(ied_src=ied_src, ied_dst=ied_dst)
        session.add(ied_src)
        session.add(ied_dst)
        session.add(goose_frame)
        session.commit()
