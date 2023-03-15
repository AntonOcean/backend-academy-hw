import asyncio
import httpx
import time

import tqdm.asyncio


ENDPOINT = "https://www.anapioficeandfire.com/api/characters/{}"


async def corutine(idx: int, client: httpx.AsyncClient):
    resp = await client.get(ENDPOINT.format(idx))
    return resp.json()["name"]


async def main():
    tasks = []
    results = []
    async with httpx.AsyncClient() as client:
        for idx in range(1, 21):
            tasks.append(asyncio.create_task(corutine(idx, client)))

        # results = await asyncio.gather(*tasks)
        for task in tqdm.asyncio.tqdm.as_completed(tasks):
            result = await task
            results.append(result)
    return results


start = time.perf_counter()
names = asyncio.run(main())
end = time.perf_counter()
for name in names:
    print(f"Name: {name}")
print(end - start)
