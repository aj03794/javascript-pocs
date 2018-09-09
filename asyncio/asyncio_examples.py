import asyncio  
import time  
from datetime import datetime

# async def or @asyncio.coroutine is the way to define an asyncio coroutine
# https://medium.freecodecamp.org/a-guide-to-asynchronous-programming-in-python-with-asyncio-232e2afa44f6

async def custom_sleep():  
    print('SLEEP {}\n'.format(datetime.now()))
    await asyncio.sleep(1)
async def factorial(name, number):  
    f = 1
    for i in range(2, number+1):
        print('Task {}: Compute factorial({})'.format(name, i))
        await asyncio.sleep(1)
        f *= i
    print('Task {}: factorial({}) is {}\n'.format(name, number, f))

start = time.time()  
loop = asyncio.get_event_loop()
tasks = [  
    asyncio.ensure_future(factorial("A", 3)),
    asyncio.ensure_future(factorial("B", 4)),
]
loop.run_until_complete(asyncio.wait(tasks))  
loop.close()
end = time.time()  
print("Total time: {}".format(end - start))

# Task A: Compute factorial(2)
# SLEEP 2018-08-19 19:17:02.369597

# Task B: Compute factorial(2)
# SLEEP 2018-08-19 19:17:02.369652

# Task A: Compute factorial(3)
# SLEEP 2018-08-19 19:17:03.370108

# Task B: Compute factorial(3)
# SLEEP 2018-08-19 19:17:03.370169

# Task A: factorial(3) is 6

# Task B: Compute factorial(4)
# SLEEP 2018-08-19 19:17:04.372917

# Task B: factorial(4) is 24

# Total time: 3.0096850395202637

# When asynchronous sleep is used (each time we call await asyncio.sleep(1)), 
# control is passed back to the event loop, 
# that runs another task from the queue (either Task A or Task B).

# In the case of standard sleep, nothing happens.
# A thread basically just hangs out. 
# In fact, because of standard sleep, 
# the current thread releases a Python interpreter, 
# and it can work with other threads if they exist, but that is another topic.




# -------------------------------------

# async def custom_sleep():  
#     print('SLEEP', datetime.now())
#     time.sleep(1)
# async def factorial(name, number):  
#     f = 1
#     for i in range(2, number+1):
#         print('Task {}: Compute factorial({})'.format(name, i))
#         await custom_sleep()
#         f *= i
#     print('Task {}: factorial({}) is {}\n'.format(name, number, f))

# start = time.time()  
# loop = asyncio.get_event_loop()
# tasks = [  
#     asyncio.ensure_future(factorial("A", 3)),
#     asyncio.ensure_future(factorial("B", 4)),
# ]
# loop.run_until_complete(asyncio.wait(tasks))  
# loop.close()
# end = time.time()  
# print("Total time: {}".format(end - start))

# Task A: Compute factorial(2)
# SLEEP 2018-08-19 19:15:57.341274
# Task A: Compute factorial(3)
# SLEEP 2018-08-19 19:15:58.346504
# Task A: factorial(3) is 6

# Task B: Compute factorial(2)
# SLEEP 2018-08-19 19:15:59.347612
# Task B: Compute factorial(3)
# SLEEP 2018-08-19 19:16:00.352843
# Task B: Compute factorial(4)
# SLEEP 2018-08-19 19:16:01.3581
# Total time: 5.0229010581970215