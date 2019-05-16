import MySQLdb
from config import MainConfig as config
import random as r
from mimesis import Datetime


def fill_users():
    db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                         passwd=config.DB_PASSWORD, db=config.DB_NAME)
    cursor = db.cursor()

    for i in config.USER_IDS:
        merchant_ids = list(range(1, len(config.MERCHANT_IDS)))
        cursor.execute("""
            INSERT INTO User (info_id, added_at, discount_category, invited_by)
            VALUES (%s, %s, %s, %s);
        """, [i, Datetime().datetime(start=2018, end=2018), r.randint(0, 30), r.choice(merchant_ids)])

    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    fill_users()
