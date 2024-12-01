import aiohttp
import asyncio

async def main():
    print('aguardnado')
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:
            await asyncio.sleep(2)
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")

asyncio.run(main())
