from fastapi import FastAPI
from pyteledantic.models import Bot, Update

import pyteledantic.methods as tg
import src.config as config

from src.handlers.base import handlers

app = FastAPI(
    title="Telegram Bot (public)",
    description="""
    A public server for processing requests from the WWW via webhooks
    """
)
bot = Bot(token=config.token)


@app.post("/send_message")
def update_handler(update: Update):
    for handler in handlers:
        if handler.is_approach(update):
            handler.func(update)


@app.get("/info")
def get_info():
    return tg.get_webhook_info(bot)


@app.on_event("startup")
def on_start():
    tg.set_webhook(bot, config.webhook_url, config.ssl_certfile)


@app.on_event("shutdown")
def on_stop():
    tg.delete_webhook(bot)
