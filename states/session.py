"""Submit-mode session state shared by handlers."""

from __future__ import annotations

from bot_core import STATE_SUBMIT_MODE, submit_mode, submit_saved_count


def enable_submit_mode(user_id: int) -> None:
    submit_mode[user_id] = True
    submit_saved_count[user_id] = 0


def disable_submit_mode(user_id: int) -> None:
    submit_mode[user_id] = False
    submit_saved_count.pop(user_id, None)


def is_submit_mode(user_id: int) -> bool:
    return bool(submit_mode.get(user_id))


__all__ = [
    "STATE_SUBMIT_MODE",
    "disable_submit_mode",
    "enable_submit_mode",
    "is_submit_mode",
    "submit_mode",
    "submit_saved_count",
]
