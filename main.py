import asyncio
import aiohttp

urls = ['http://google.com', 'http://localhost:5000/', 'http://localhost:5000/']

# url = 'http://localhost:5000/'


async def call_url(url):
    print('Starting {}'.format(url))
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            status = response.status
            # statusCode = response.statusCode
            print('url : {}, data length: {}, status: {}'.format(url, len(data), status))
            return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))



# http://localhost:5000/: 29
# http://localhost:5000/: 29
# http://google.com: 10815

# --------------------------------------------


# async def fetch(session, url):
#     print('Fetching')
#     async with session.get(url) as response:
#         return await response.text()

# async def main():
#     async with aiohttp.ClientSession() as session:
#         for url in urls:
#             print(url)
#             html = await fetch(session, url)
#             print(html)
       

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())