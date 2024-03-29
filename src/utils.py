from pyteledantic.models import MessageToSend, Message

import pyteledantic.methods as tg
import aiohttp, asyncio

from src.model import Moderator
from src.config import token


async def notify_moderators(text: str):
    moderators: list[Moderator] = Moderator.select()
    if moderators:
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        async with aiohttp.ClientSession() as session:
            tasks = []
            for moderator in moderators:
                message = MessageToSend(chat_id=moderator.telegram_id, text=text, parse_mode="MarkdownV2")
                await session.post(url, data=message.dict())
            # await asyncio.wait(tasks)


def send_message(user: int, text: str):
    tg.send_message(token, MessageToSend(chat_id=user, text=text, parse_mode="MarkdownV2"))