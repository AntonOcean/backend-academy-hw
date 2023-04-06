import requests
import time
import tqdm

ENDPOINT = "https://www.anapioficeandfire.com/api/characters/{}"


def f():
    result = []
    for idx in tqdm.tqdm(range(1, 21)):
        resp = requests.get(ENDPOINT.format(idx))
        assert resp.status_code == 200
        result.append(resp.json()["name"])
    return result


start = time.perf_counter()
names = f()
end = time.perf_counter()
for name in names:
    print(f"Name: {name}")
print(end - start)
