import MySQLdb
from config import MainConfig as config
import itertools as it
import random as r
from mimesis import Datetime

db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER, passwd=config.DB_PASSWORD, db=config.DB_NAME)
c = db.cursor()

for i in range(2, int(config.N_PERSONS/10)):
    c.execute("""
        INSERT INTO `Order` (merchant_id, completed_at, user_id)
        VALUES (%s, %s, %s);
    """, [i, Datetime().datetime(), r.randint(int(config.N_PERSONS/10) + 2, config.N_PERSONS)])
db.commit()

c.close()
db.close()

