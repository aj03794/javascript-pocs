import asyncio

async def say(what, when):
    print('asdf')
    await asyncio.sleep(when)
    print(what)

# Get this error when trying to close an even tloop that is running forever
# RuntimeError("Cannot close a running event loop")
async def close(loop, when):
    print('Closing loop')
    await asyncio.sleep(when)
    # loop.close()

loop = asyncio.get_event_loop()

loop.create_task(say('first hello', 2))
loop.create_task(say('second hello', 1))
loop.create_task(close(loop, 3))

loop.run_forever()
# This never prints and the loop never closes
print('LOOP IS CLOSING')
loop.close()