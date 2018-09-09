##### Things learned

- Lists replace arrays


- Array of lambda functions
```
routes = [
    lambda: print('hello') ,
    lambda: print('Bye'),
    lambda: print('Test1')
]
```

```
routes = [
    lambda: (
    #    @app.route('/test', methods=['POST'])
       lambda: (
           print('This is my lambda function')
       )
    ),
]

for route in routes:
    print('route', route)
    print(route()())

Prints 'This is my lambda function'
```

###### Dictionary keys in array

- `print('Dictionary keys as an array', [*databaseFuncs])`

###### Asyncio

- Invoking a function that has the `async` keyword infront of it returns a coroutine object

```
async def steps(x):
    result = await multiply(x)
    print("result: %s" % result)
loop = asyncio.get_event_loop()
# coro stands for coroutine
coro = steps(5)
<!-- coro <coroutine object steps at 0x101404af0> -->
```