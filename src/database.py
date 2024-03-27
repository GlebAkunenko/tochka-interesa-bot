from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector import connect

from src.model import Moderator

import src.config as config


def create_connection() -> PooledMySQLConnection | MySQLConnectionAbstract:
    return connect(
      host=config.host,
      user=config.user,
      password=config.password,
      database=config.database_name
    )


with create_connection() as conn, conn.cursor(dictionary=True) as cursor:
    cursor.execute("select * from moderators")
    _data = cursor.fetchall()
    moderators: list[Moderator] = [Moderator.parse_obj(d) for d in _data]