"""User, goal, achievement, and support-message database operations."""

from __future__ import annotations

from bot_core import (
    add_support_message,
    block_user,
    count_records,
    count_records_between,
    count_records_today,
    delete_goal,
    get_goal,
    get_user,
    get_user_achievements,
    load_support,
    load_users,
    mark_support_replied,
    parse_admin_target,
    register_user,
    remove_user,
    set_user_note,
    set_user_sheet,
    unblock_user,
    update_last_active,
    upsert_goal,
)

__all__ = [
    "add_support_message",
    "block_user",
    "count_records",
    "count_records_between",
    "count_records_today",
    "delete_goal",
    "get_goal",
    "get_user",
    "get_user_achievements",
    "load_support",
    "load_users",
    "mark_support_replied",
    "parse_admin_target",
    "register_user",
    "remove_user",
    "set_user_note",
    "set_user_sheet",
    "unblock_user",
    "update_last_active",
    "upsert_goal",
]
