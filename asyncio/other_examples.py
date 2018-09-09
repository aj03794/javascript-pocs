import asyncio

async def multiply(x):
    result = x * 2
    await asyncio.sleep(1)
    return result


async def steps(x):
    result = await multiply(x)
    print("result: %s" % result)


loop = asyncio.get_event_loop()
# coro stands for coroutine
coro = steps(5)
print('coro', coro)
loop.run_until_complete(coro)
loop.close()

