import MySQLdb
from config import MainConfig as config
import random as r


def fill_gifts():
    db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                         passwd=config.DB_PASSWORD, db=config.DB_NAME)
    cursor = db.cursor()

    names = ['Открытка', 'Игрушка мишки', 'Упаковка к цветам', 'Брелок', 'Игрушка сердце']

    for name in names:
        cursor.execute("""
            INSERT INTO Gift (name, current_price, available)
            VALUES (%s, %s, %s);
        """, [name, r.randint(50, 600), r.randint(1, 300)])

    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    fill_gifts()
