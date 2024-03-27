from pyteledantic.models import Message

from src.handlers.base import Handler
from src.database import create_connection, moderators
from src.model import Moderator

import datetime as dt

handler = Handler()

@handler.command("/subscribe")
def subscribe(message: Message):
    user = message.from_user.id
    if user in [m.telegram_id for m in moderators]:
        return "Ты уже модератор"
    with create_connection() as conn, conn.cursor() as cursor:
        mod = Moderator(
            id=0,
            name=message.from_user.username,
            telegram_id=message.from_user.id,
            is_superuser=False,
            hiring_date=dt.datetime.now()
        )
        cursor.execute(f"""
        insert into moderators (name, telegram_id, is_superuser, hiring_date) value (
            '{mod.name}',
            {mod.telegram_id},
            0,
            '{mod.hiring_date}'
        )
        """)
        conn.commit()
        mod.id = cursor.lastrowid
        moderators.append(mod)
        return "Теперь ты модератор"


@handler.command("/unsubscribe")
def unsubscribe(message: Message):
    user = message.from_user.id
    if user not in [m.telegram_id for m in moderators]:
        return "Ты и так не модератор"
    with create_connection() as conn, conn.cursor() as cursor:
        cursor.execute(f"delete from moderators where telegram_id = '{message.from_user.id}'")
        conn.commit()
        for m in moderators:
            if m.telegram_id == user:
                moderators.remove(m)
        return "Теперь ты не модератор"
