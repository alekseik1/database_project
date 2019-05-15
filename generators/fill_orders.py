import MySQLdb
from config import MainConfig as config
import random as r
from mimesis import Datetime


def fill_orders(cursor):
    for i in range(60):
        print(i)
        cursor.execute("""
            INSERT INTO `Order` (merchant_id, completed_at, user_id)
            VALUES (%s, %s, %s);
        """, [
                r.choice(config.MERCHANT_IDS[:-1]),
                Datetime().datetime(),
#                r.choice(config.USER_IDS[:-1])
                1
            ]
        )


if __name__ == '__main__':
    db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                         passwd=config.DB_PASSWORD, db=config.DB_NAME)
    c = db.cursor()
    fill_orders(c)
    db.commit()
    c.close()
    db.close()
