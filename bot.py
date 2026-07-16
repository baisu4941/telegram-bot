"""Main Telegram bot entrypoint.

This file intentionally stays small: it loads configuration, initializes
storage, registers Telegram handlers, and starts polling.
"""

from __future__ import annotations

import logging

from telegram import Update
from telegram.ext import Application
from telegram.request import HTTPXRequest

import config
from database.db import init_storage
from handlers.callbacks import post_init, register_handlers


logging.basicConfig(
    filename=config.LOG_FILE,
    filemode="a",
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger("fb_data_bot")


def build_application() -> Application:
    """Create and configure the python-telegram-bot Application."""
    request = HTTPXRequest(
        connect_timeout=30.0,
        read_timeout=30.0,
        write_timeout=30.0,
        pool_timeout=30.0,
    )

    app = (
        Application.builder()
        .token(config.BOT_TOKEN)
        .request(request)
        .post_init(post_init)
        .build()
    )
    register_handlers(app)
    return app


def main() -> None:
    """Initialize dependencies and run the Telegram polling loop."""
    if not config.BOT_TOKEN:
        raise ValueError("Set BOT_TOKEN in .env or environment variables.")
    if config.ADMIN_ID == 0:
        raise ValueError("Set ADMIN_ID in .env or environment variables.")

    init_storage()
    app = build_application()

    print("FB Data Bot is starting...")
    logger.info("FB Data Bot is starting")
    app.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True,
        poll_interval=1.0,
        timeout=30,
    )


if __name__ == "__main__":
    main()
