import MySQLdb
from config import MainConfig as config
import random as r
from mimesis import Datetime


def fill_mercants():
    db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                         passwd=config.DB_PASSWORD, db=config.DB_NAME)
    cursor = db.cursor()

    for i in config.MERCHANT_IDS:
        cursor.execute("""
            INSERT INTO Merchant (info_id, added_at, access_level)
            VALUES (%s, %s, %s);
        """, [i, Datetime().datetime(start=2018, end=2018), r.randint(0, 3)])

    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    fill_mercants()
