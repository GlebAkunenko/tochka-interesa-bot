from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector import connect

import src.config as config


def create_connection() -> PooledMySQLConnection | MySQLConnectionAbstract:
    return connect(
      host=config.host,
      user=config.user,
      password=config.password,
      database=config.database_name
    )