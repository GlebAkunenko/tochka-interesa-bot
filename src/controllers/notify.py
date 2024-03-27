from fastapi import Depends
from fastapi.routing import APIRouter
from pyteledantic.models import Bot, MessageToSend

from src.model import Moderator

import pyteledantic.methods as tg
import src.config as config

router = APIRouter(prefix="/notify")
bot = Bot(token=config.token)

@router.post("/server")
def server_status(server: str, is_active: bool):
    moderators: list[Moderator] = Moderator.select()
    if moderators:
        for moderator in moderators:
            tg.send_message(bot.token, MessageToSend(
                chat_id=moderator.telegram_id,
                text=f"*{server}* {'запущен ✅' if is_active else 'остановлен ❌'}",
                parse_mode="MarkdownV2"
            ))