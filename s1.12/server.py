from aiohttp import web, ClientSession
import asyncio
import time


async def handle(request):
    # time.sleep(2)
    # await asyncio.sleep(2)
    name = request.match_info.get('name')
    if name:
      text = f'Hello {name}\n'
    else:
        async with ClientSession() as session:
            async with session.get('http://localhost:8081/Anon') as response:
                text = await response.text()
    print('info')
    return web.Response(text=text)


app = web.Application()
app.add_routes([
    web.get('/', handle),
    web.get('/{name}', handle),
])


web.run_app(app)

# loop = asyncio.get_event_loop()
# await loop.run_in_executor()