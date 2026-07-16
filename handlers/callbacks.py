"""Inline callback routing and handler registration."""

from __future__ import annotations

from telegram import Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from bot_core import (
    button_callback,
    cmd_block,
    cmd_broadcast,
    cmd_cancel,
    cmd_done,
    cmd_fbdata,
    cmd_goal,
    cmd_msg,
    cmd_note,
    cmd_remove,
    cmd_settings,
    cmd_stats,
    cmd_support,
    cmd_unblock,
    cmd_userinfo,
    cmd_users,
    error_handler,
    handle_message,
    post_init,
    start,
)


def register_handlers(app: Application) -> None:
    """Register all Telegram commands, callbacks, messages, and errors."""
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cancel", cmd_cancel))
    app.add_handler(CommandHandler("done", cmd_done))
    app.add_handler(CommandHandler("goal", cmd_goal))
    app.add_handler(CommandHandler("settings", cmd_settings))

    app.add_handler(CommandHandler("users", cmd_users))
    app.add_handler(CommandHandler("userinfo", cmd_userinfo))
    app.add_handler(CommandHandler("support", cmd_support))
    app.add_handler(CommandHandler("stats", cmd_stats))
    app.add_handler(CommandHandler("block", cmd_block))
    app.add_handler(CommandHandler("unblock", cmd_unblock))
    app.add_handler(CommandHandler("remove", cmd_remove))
    app.add_handler(CommandHandler("note", cmd_note))
    app.add_handler(CommandHandler("broadcast", cmd_broadcast))
    app.add_handler(CommandHandler("msg", cmd_msg))
    app.add_handler(CommandHandler("fbdata", cmd_fbdata))

    app.add_handler(CallbackQueryHandler(button_callback))
    app.add_handler(MessageHandler((filters.TEXT | filters.CAPTION) & ~filters.COMMAND, handle_message))
    app.add_error_handler(error_handler)


__all__ = [
    "button_callback",
    "error_handler",
    "post_init",
    "register_handlers",
]
