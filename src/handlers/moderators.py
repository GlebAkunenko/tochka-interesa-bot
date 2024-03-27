from pyteledantic.models import Message

from src.handlers.base import Handler
from src.database import create_connection

import datetime as dt

handler = Handler()

@handler.command("/subscribe")
def subscribe(message: Message):
    with create_connection() as conn, conn.cursor() as cursor:
        cursor.execute(f"""
        insert into moderators (name, telegram_id, is_superuser, hiring_date) value (
            '{message.from_user.username}',
            '{message.from_user.id}',
            0,
            '{dt.datetime.now()}'
        )
        """)
        conn.commit()


@handler.command("/unsubscribe")
def unsubscribe(message: Message):
    with create_connection() as conn, conn.cursor() as cursor:
        cursor.execute(f"delete from moderators where telegram_id = '{message.from_user.id}'")
        conn.commit()