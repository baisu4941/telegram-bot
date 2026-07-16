"""Submit Mode activation, UID validation, and auto-save handling."""

from __future__ import annotations

from bot_core import (
    _handle_submit_mode_uid,
    _process_submit_mode_message_sync,
    _queue_fb_batch_message,
    handle_message,
    submit_text,
)

__all__ = [
    "_handle_submit_mode_uid",
    "_process_submit_mode_message_sync",
    "_queue_fb_batch_message",
    "handle_message",
    "submit_text",
]
