from sqlalchemy import Engine
from sqlalchemy.orm import Session

from src.models.alerts.integrity_alert import GooseIntegrityAlert
from src.models.goose_frame import GooseFrame
from src.models.ied import IED


def generate_integrity_alert(engine: Engine, *, with_fixed: bool = False) -> None:
    with Session(engine) as session:
        ied_src = IED.build(name="src")
        ied_dst = IED.build(name="dst")
        goose_frame = GooseFrame.build(ied_src=ied_src, ied_dst=ied_dst)
        session.add(ied_src)
        session.add(ied_dst)
        session.add(goose_frame)
        if with_fixed:
            integrity_alert_fix = GooseIntegrityAlert.build(
                goose_frame_id=goose_frame.id, value="correct", error=False,
            )
            session.add(integrity_alert_fix)
        session.add(GooseIntegrityAlert.build(goose_frame_id=goose_frame.id, value="problem"))
        session.commit()
