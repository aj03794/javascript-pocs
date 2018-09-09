from functools import partial

def example(argument1):
    return partial()



x = lambda firstArg: lambda secondArg: lambda thirdArg: (
    some_func()
)

def some_func():
    print('hello')

x(1)(2)(3)




def multiply(x,y):
        return x * y

# create a new function that multiplies by 2
print(partial(multiply,2)(4))

