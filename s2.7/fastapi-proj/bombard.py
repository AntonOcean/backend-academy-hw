import asyncio
import random

import requests
from faker import Faker

ENDPOINT = "http://localhost:8000/character/{}"
ENDPOINT2 = "http://localhost:8000/character"
ENDPOINT3 = "http://localhost:8000/characters"


POST_ENDPOINT = ""


def main():
    f = Faker()
    while True:
        rand = random.randint(0, 4)
        if rand == 0:
            _ = requests.get(ENDPOINT.format(random.randint(0, 100)))
        elif rand == 1:
            _ = requests.get(ENDPOINT2)
        elif rand == 2:
            _ = requests.get(ENDPOINT3)
        else:
            payload = {
                "name": f.name(),
                "culture": f.name(),
                "gender": random.choice(
                    [
                        "Male",
                        "Female",
                    ]
                ),
                "has_spouse": bool(random.randint(0, 1)),
            }
            _ = requests.post(ENDPOINT2, json=payload)


main()
