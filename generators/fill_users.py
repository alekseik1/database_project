import MySQLdb
from config import MainConfig as config
import itertools as it
import random as r
from mimesis import Datetime

db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER, passwd=config.DB_PASSWORD, db=config.DB_NAME)
c = db.cursor()

for i in range(int(config.N_PERSONS/10) + 2, config.N_PERSONS):
    c.execute("""
        INSERT INTO User (info_id, added_at, discount_category, invited_by)
        VALUES (%s, %s, %s, %s);
    """, [i, Datetime().datetime(), r.randint(0, 30), 3])
db.commit()

c.close()
db.close()

