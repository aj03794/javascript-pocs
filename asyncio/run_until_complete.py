import asyncio

from pydash import at

def do_async(futures):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
    loop.close()

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

# loop = asyncio.get_event_loop()

# futures = [
#     asyncio.ensure_future(create_customer()),
#     asyncio.ensure_future(update_customer()),
#     asyncio.ensure_future(delete_customer()),
#     asyncio.ensure_future(read_customer())
# ]

# do_async(futures)
# print('Asyncio loop complete')
# loop.close()

# Doing the below throws an error currently
# RecursionError: maximum recursion depth exceeded

funcs = {
    'create_customer': lambda: do_async([ create_customer() ]),
    'update_customer': lambda: update_customer(),
    'delete_customer': lambda: delete_customer(),
    'read_customer': lambda: read_customer()
}

create_customer, update_customer, read_customer, delete_customer = at(
funcs,
'create_customer',
'update_customer',
'read_customer',
'delete_customer'
)

# create_customer()



# -----------------------------------------------

# Asyncio basic example

def run_until_complete():

    async def say(what, when):
        await asyncio.sleep(when)
        print(what)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(say('hello world', 1))
    loop.close()

run_until_complete()
