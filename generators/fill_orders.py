import MySQLdb
from config import MainConfig as config
import itertools as it
import random as r
from mimesis import Datetime

db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER, passwd=config.DB_PASSWORD, db=config.DB_NAME)
c = db.cursor()

for i in range(60):
    c.execute("""
        INSERT INTO `Order` (merchant_id, completed_at, user_id)
        VALUES (%s, %s, %s);
    """, [
        r.choice(config.MERCHANT_IDS),
        Datetime().datetime(),
        #r.choice(config.USER_IDS)
        20
        ]
    )
db.commit()

c.close()
db.close()

