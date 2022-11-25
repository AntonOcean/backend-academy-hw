import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()  # return yield from
        else:
            return f'ERROR: {response.status}'


async def download_wiki(article):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://de.wikipedia.org/{}'.format(article))
        return html[:15]

# в одном треде ждем много вещей
loop = asyncio.get_event_loop()

args = ['wiki/Évariste_Galois', 'wiki/Alan_Turing', 'zzz']

tasks1 = asyncio.gather(
    download_wiki('wiki/Évariste_Galois'), download_wiki('zzz')
)

tasks2 = asyncio.gather(
    download_wiki('wiki/Alan_Turing')
)

tasks = asyncio.gather(tasks1, tasks2)

print(loop.run_until_complete(tasks))