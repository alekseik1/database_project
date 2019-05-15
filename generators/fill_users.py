import MySQLdb
from config import MainConfig as config
import random as r
from mimesis import Datetime


def fill_users(cursor):
    for i in config.USER_IDS:
        cursor.execute("""
            INSERT INTO User (info_id, added_at, discount_category, invited_by)
            VALUES (%s, %s, %s, %s);
        """, [i, Datetime().datetime(), r.randint(0, 30), 3])


if __name__ == '__main__':
    db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                         passwd=config.DB_PASSWORD, db=config.DB_NAME)
    c = db.cursor()
    fill_users(c)
    db.commit()
    c.close()
    db.close()
