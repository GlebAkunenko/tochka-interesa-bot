from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector import connect
from redis_cache import RedisCache
from redis import Redis

from src.model import Moderator

import src.config as config



def create_connection() -> PooledMySQLConnection | MySQLConnectionAbstract:
    return connect(
      host=config.host,
      user=config.user,
      password=config.password,
      database=config.database_name
    )


cache = RedisCache(
    redis_client=Redis(host=config.redis_host),
    prefix="bot-cache"
)

@cache.cache(ttl=10)
def get_moderators():
    with create_connection() as conn, conn.cursor(dictionary=True) as cursor:
        cursor.execute("select * from moderators")
        data = cursor.fetchall()
        return [Moderator.parse_obj(d) for d in data]
