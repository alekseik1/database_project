import MySQLdb
from config import MainConfig as config
from mimesis import Person, Datetime


def fill_persondata():
    db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                         passwd=config.DB_PASSWORD, db=config.DB_NAME)
    cursor = db.cursor()

    # Zero client, anon
    cursor.execute("""INSERT INTO PersonData (first_name, last_name, birth_date, email, mobile, gender) VALUES (%s, %s, %s, %s,
            %s, %s);""",
              ['anon', 'anon', Datetime().date(start=1950, end=2001), None, None, None])
    for _ in range(config.N_PERSONS):
        p = Person('ru')
        cursor.execute("""INSERT INTO PersonData (first_name, last_name, birth_date, email, mobile, gender) VALUES (%s, %s, %s,
                %s, %s, %s);""", [
            p.name(), p.surname(), Datetime().date(start=1950, end=2001),
            p.email(), p.telephone('#'*11),
            'M' if p.gender(iso5218=True) == 1 else 'F'
        ])

    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    fill_persondata()
