"""Main module to run database."""
from threading import Thread
from time import sleep

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.models.alerts.integrity_alert import FieldsEnum, GooseIntegrityAlert
from src.models.alerts.message_alert import GooseMessageAlert
from src.models.base import Base
from src.models.goose_frame import GooseFrame
from src.models.ied import IED
from src.services.alert_handler import AlertHandler


def main() -> None:
    """."""
    engine = create_engine("sqlite:///database.db", echo=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    alert_handler = AlertHandler(engine=engine)
    alert_handler_thread = Thread(target=alert_handler.process, daemon=True)
    alert_handler_thread.start()
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
        integrity_alert = GooseIntegrityAlert(
            goose_frame_id=goose_frame.id,
            field=FieldsEnum.GOOSE_ID,
            error=True,
            value="test2",
        )
        message_alert = GooseMessageAlert(
            goose_frame_id=goose_frame.id,
            abscense=True,
        )
        alert_handler.add(integrity_alert)
        alert_handler.add(message_alert)

    sleep(1)

if __name__ == "__main__":
    main()
