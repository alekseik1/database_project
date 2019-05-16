class MainConfig:

    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'toor'
    DB_NAME = 'flower_shop'
    N_PERSONS = 150
    N_ORDERS = 5325
    MERCHANT_IDS = list(range(2, 10))
    USER_IDS = sorted(list(set(range(1, int(N_PERSONS/2))) - set(MERCHANT_IDS)))
