from faker import Faker
import random
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost", database="foo", user="postgres", password="postgres"
)

# Create a cursor object
cur = conn.cursor()

# Create a Faker instance
fake = Faker()

# Generate fake data and insert it into the database
for i in range(10):
    name = fake.name()
    cur.execute("INSERT INTO person (id, name) VALUES (%s, %s)", (i + 1, name))

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
