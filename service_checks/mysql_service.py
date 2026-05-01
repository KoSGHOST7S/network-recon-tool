"""MySQL service check.

Implements the same pattern as your provided mysqlCheck script:
- open MySQL connection with credentials
- run a basic query
- treat successful query as successful service check
"""

from __future__ import annotations

import pymysql

MYSQL_USER = "admin"
MYSQL_PASSWORD = "admin"
MYSQL_DATABASE = "test"
MYSQL_QUERY = "select * from test"


def run(target_ip: str, target_name: str) -> bool:
    """Return True when MySQL login and query execution succeed."""
    db_conn = None
    try:
        db_conn = pymysql.connect(
            host=target_ip,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            ssl=None,
            connect_timeout=5,
        )
        with db_conn.cursor() as db_cursor:
            db_cursor.execute(MYSQL_QUERY)
            db_cursor.fetchone()
        return True
    except Exception:
        return False
    finally:
        if db_conn is not None:
            db_conn.close()

