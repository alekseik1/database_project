import MySQLdb
from config import MainConfig as config
import random as r
from mimesis import Datetime


def fill_mercants(cursor):
    for i in config.MERCHANT_IDS:
        cursor.execute("""
            INSERT INTO Merchant (info_id, added_at, access_level)
            VALUES (%s, %s, %s);
        """, [i, Datetime().datetime(), r.randint(0, 3)])


if __name__ == '__main__':
    db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                         passwd=config.DB_PASSWORD, db=config.DB_NAME)
    c = db.cursor()
    fill_mercants(c)
    db.commit()
    c.close()
    db.close()
