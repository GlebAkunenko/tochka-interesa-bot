from pyteledantic.models import Message

from src.handlers.base import Handler
from src.database import create_connection
from src.model import Moderator

import datetime as dt

handler = Handler()


# @handler.command("/start")
# def start(message: Message):
#     ...


@handler.command("/subscribe")
def subscribe(message: Message):
    user = message.from_user.id
    if Moderator.select(ids=[user]):
        return "Ты уже модератор"
    user = message.from_user
    name = f"{user.first_name if user.first_name else ''} {user.last_name if user.last_name else ''}"
    Moderator.insert(Moderator(
        name=name,
        username=user.username,
        telegram_id=user.id,
        is_superuser=False,
        hiring_date=dt.datetime.now()
    ))
    return "Теперь ты модератор"


@handler.command("/unsubscribe")
def unsubscribe(message: Message):
    user = message.from_user.id
    if not Moderator.select(ids=[user]):
        return "Ты и так не модератор"
    Moderator.delete(ids=user)
    return "Теперь ты не модератор"
