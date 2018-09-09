import asyncio
    
def do_async(futures):
    print('Futures', futures)
    loop = asyncio.get_event_loop()
    # loop.run_forever(asyncio.wait(futures))
    loop.run_forever

async def create_customer():
    print('Creating customer')
    await asyncio.sleep(1)
    print('Customer created!')
    return      

async def update_customer():
    print('Updating customer...')
    await asyncio.sleep(1)
    print('Customer updated!')
    return

async def delete_customer():
    print('Deleting customer...')
    await asyncio.sleep(1)
    print('Customer deleted!')
    return

async def read_customer():
    print('Reading customer...')
    await asyncio.sleep(1)
    print('Customer read!')
    return

futures = [
    asyncio.ensure_future(create_customer()),
    asyncio.ensure_future(update_customer()),
    asyncio.ensure_future(delete_customer()),
    asyncio.ensure_future(read_customer())
]

do_async(futures)
print('Asyncio loop complete')