import uuid
import pandas as pd

from faker import Faker

FAKE = Faker(locale='ru_RU')

COUNT = 1_000_000

DATA = {
    'id': [],
    'first_name': [],
    'last_name': [],
    'text': []
}


def generate_one():
    id = uuid.uuid4()
    last_name = FAKE.last_name()
    first_name = FAKE.first_name()
    text = FAKE.text()

    DATA['id'].append(id)
    DATA['last_name'].append(last_name)
    DATA['first_name'].append(first_name)
    DATA['text'].append(text)


def main():
    for _ in range(COUNT):
        generate_one()

    df = pd.DataFrame(DATA)
    df.to_csv('data.csv', index=False)


if __name__ == '__main__':
    main()
