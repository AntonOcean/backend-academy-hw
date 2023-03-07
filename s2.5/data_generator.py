import random
import uuid

import psycopg2
from faker import Faker

fake = Faker(locale='ru_RU')

COUNT = 1_000

# # Connect to your postgres DB
conn = psycopg2.connect(
    host='127.0.0.1',
    port=5432,
    database='mydb',
    user='postgres',
    password='postgres'
)
#
# # Open a cursor to perform database operations
with conn.cursor() as cur:
    #
    template = '''
    INSERT INTO person (name, last_name, balance_max, code, joined_at, balance_min)
    VALUES {};
    '''

    template_one = '''('{}', '{}', {}, '{}', '{}', {})'''

    print("start")

    data = [template_one.format(
        fake.first_name(),
        fake.last_name(),
        random.randint(100, 1000),
        uuid.uuid4(),
        fake.date(),
        random.randint(1, 100)
    ) for i in range(COUNT)]

    print("data ready")
    cur.execute(template.format(','.join(data)))

    print("insert ready")
    conn.commit()

    print("close....")

conn.close()
