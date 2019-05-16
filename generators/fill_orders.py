import MySQLdb
from config import MainConfig as config
import random as r
from mimesis import Datetime


def fill_orders():
    db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                         passwd=config.DB_PASSWORD, db=config.DB_NAME)
    cursor = db.cursor()

    for i in range(config.N_ORDERS):
        user_id = r.choice(range(1, len(config.USER_IDS)))
        cursor.execute("""
            INSERT INTO `Order` (merchant_id, completed_at, user_id, total_sum)
            VALUES (%s, %s, %s, %s);
        """, [
                r.choice(config.MERCHANT_IDS[:-1]),
                Datetime().datetime(start=2018, end=2018),
                user_id,
                r.randint(200, 600)
            ]
        )

    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    fill_orders()
