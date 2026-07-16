"""Input parsing and UID validation helpers."""

from __future__ import annotations

from bot_core import (
    _extract_submit_uid,
    clean_sheet_id,
    normalize_submission_input,
    parse_goal_input,
    parse_record_input,
)


def is_valid_uid(text: str) -> bool:
    """Return True when text contains one valid submit UID."""
    return _extract_submit_uid(text) is not None


__all__ = [
    "_extract_submit_uid",
    "clean_sheet_id",
    "is_valid_uid",
    "normalize_submission_input",
    "parse_goal_input",
    "parse_record_input",
]
