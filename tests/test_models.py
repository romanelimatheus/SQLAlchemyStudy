import pytest

from src.models.alerts.alert_lobby import AlertsEnum, AlertsLobby
from src.models.alerts.integrity_alert import GooseIntegrityAlert
from src.models.alerts.message_alert import GooseMessageAlert


class TestAlertLobby:
    def test_from_alert(self: "TestAlertLobby") -> None:
        alert = GooseIntegrityAlert.default()
        alert_lobby = AlertsLobby.from_alert(alert)
        assert alert_lobby.alert_reference == AlertsEnum.INTEGRITY
        assert alert_lobby.alert_id == alert.id

class TestAlertsEnum:
    def test_from_instance_integrity(self: "TestAlertsEnum") -> None:
        alert = AlertsEnum.from_instance(GooseIntegrityAlert.default())
        assert alert == AlertsEnum.INTEGRITY

    def test_from_instance_message(self: "TestAlertsEnum") -> None:
        alert = AlertsEnum.from_instance(GooseMessageAlert.default())
        assert alert == AlertsEnum.MESSAGE

    def test_from_unknown(self: "TestAlertsEnum") -> None:
        msg = "Unknown alert type: <class 'NoneType'>"
        with pytest.raises(ValueError, match=msg):
            AlertsEnum.from_instance(None) # type: ignore  # noqa: PGH003
