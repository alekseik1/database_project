import MySQLdb
from config import MainConfig as config
import random as r
from mimesis import Datetime


def fill_orders():
    db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                         passwd=config.DB_PASSWORD, db=config.DB_NAME)
    cursor = db.cursor()

    for i in range(60):
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

    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    fill_orders()
