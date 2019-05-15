import MySQLdb
from config import MainConfig as config
import itertools as it
import random as r


def fill_flowers():
    db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                         passwd=config.DB_PASSWORD, db=config.DB_NAME)
    cursor = db.cursor()

    flowers = ['Гвоздика', 'Роза', 'Тюльпан', 'Орхидея', 'Нарцисс']
    colors = ['RED', 'YELLOW', 'BLUE', 'BLACK', 'WHITE']

    for flower, color in it.product(flowers, colors):
        cursor.execute("""
            INSERT INTO Flower (name, color, current_price, available)
            VALUES (%s, %s, %s, %s);
        """, [flower, color, r.randint(50, 600), r.randint(1, 300)])

    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    fill_flowers()
