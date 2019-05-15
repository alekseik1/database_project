import MySQLdb
from config import MainConfig as config
import random as r


def fill_ordergifts():
    db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                         passwd=config.DB_PASSWORD, db=config.DB_NAME)
    cursor = db.cursor()

    names = ['Открытка', 'Игрушка мишки', 'Упаковка к цветам', 'Брелок', 'Игрушка сердце']

    gift_ids = range(1, len(names))
    order_ids = range(1, config.N_ORDERS)

    for order_id in order_ids:
        # Покупается 1 тип игрушки
        for gift_id in r.choices(gift_ids, k=1):
            cursor.execute("""
                INSERT INTO OrderGift (order_id, gift_id, quantity)
                VALUES (%s, %s, %s);
            """, [order_id, gift_id, r.randint(1, 3)])

    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    fill_ordergifts()
