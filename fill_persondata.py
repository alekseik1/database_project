import MySQLdb
from config import MainConfig as config
import itertools as it
import random as r
from mimesis import Person, Datetime

db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER, passwd=config.DB_PASSWORD, db=config.DB_NAME)
c = db.cursor()

# Zero client, anon
c.execute("""INSERT INTO PersonData (first_name, last_name, birth_date, email, mobile, gender) VALUES (%s, %s, %s, %s,
        %s, %s);""", ['anon', 'anon', Datetime().date(), None, None, None])

N_clients = config.N_PERSONS
for _ in range(N_clients):
    p = Person('ru')
    c.execute("""INSERT INTO PersonData (first_name, last_name, birth_date, email, mobile, gender) VALUES (%s, %s, %s,
            %s, %s, %s);""", [p.name(), p.surname(), Datetime().date(), p.email(), p.telephone('#'*11), 'M' if p.gender(iso5218=True)==1 else 'F'])
db.commit()

c.close()
db.close()

