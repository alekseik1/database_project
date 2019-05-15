import MySQLdb
from config import MainConfig as config

from fill_flowers import fill_flowers
from fill_gifts import fill_gifts
from fill_persondata import fill_persondata
from fill_merchants import fill_mercants
from fill_users import fill_users
from fill_orders import fill_orders

if __name__ == '__main__':
    db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                         passwd=config.DB_PASSWORD, db=config.DB_NAME)
    c = db.cursor()

    fill_flowers(c)
    fill_gifts(c)
    fill_persondata(c)
    fill_mercants(c)
    fill_users(c)
    fill_orders(c)

    db.commit()
    c.close()
    db.close()
