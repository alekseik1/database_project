import MySQLdb
from config import MainConfig as config
import random as r


def fill_flowers():
    db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                         passwd=config.DB_PASSWORD, db=config.DB_NAME)
    cursor = db.cursor()

    flowers = ['Гвоздика', 'Роза', 'Тюльпан', 'Орхидея', 'Нарцисс']
    colors = ['RED', 'YELLOW', 'BLUE', 'BLACK', 'WHITE']

    flower_ids = range(1, len(flowers)*len(colors))
    order_ids = range(1, config.N_ORDERS)

    for order_id in order_ids:
        for flower_id in r.choices(flower_ids, k=2):
            cursor.execute("""
                INSERT INTO OrderFlower (order_id, flower_id, quantity)
                VALUES (%s, %s, %s);
            """, [order_id, flower_id, r.randint(1, 3)])

    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    fill_flowers()
