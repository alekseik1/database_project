import MySQLdb
from config import MainConfig as config

from fill_flowers import fill_flowers
from fill_gifts import fill_gifts
from fill_persondata import fill_persondata
from fill_merchants import fill_mercants
from fill_users import fill_users
from fill_orders import fill_orders

if __name__ == '__main__':
    fill_flowers()
    fill_gifts()
    fill_persondata()
    fill_mercants()
    fill_users()
    fill_orders()

