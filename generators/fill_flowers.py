import MySQLdb
from config import MainConfig as config
import itertools as it
import random as r

db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER, passwd=config.DB_PASSWORD, db=config.DB_NAME)
c = db.cursor()

flowers = ['Гвоздика', 'Роза', 'Тюльпан', 'Орхидея', 'Нарцисс']
colors = ['RED', 'YELLOW', 'BLUE', 'BLACK', 'WHITE']

for flower, color in it.product(flowers, colors):
    c.execute("""
        INSERT INTO Flower (name, color, current_price, available)
        VALUES (%s, %s, %s, %s);
    """, [flower, color, r.randint(50, 600), r.randint(1, 300)])
db.commit()

c.close()
db.close()

