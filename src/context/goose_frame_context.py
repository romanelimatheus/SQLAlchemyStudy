"""Access infos based on goose frame."""
from sqlalchemy import Select, select

from src.models.goose_frame import GooseFrame


class GooseFrameContext:
    """Context based on goose frame."""

    def get_goose_frames(self: "GooseFrameContext") -> Select[tuple[GooseFrame]]:
        """Get goose frames with ied info."""
        return select(GooseFrame)
