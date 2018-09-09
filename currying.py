from pydash import curry
from promise import Promise

# def currying_func(arg1, arg2, arg3):
#     print(arg1)
#     print(arg2)
#     print(arg3)

# currying_func = curry(currying_func)

# print(currying_func)

# currying_func(1, 2)(3)

# # OR

# currying_func = currying_func(1)
# currying_func = currying_func(2)
# currying_func = currying_func(3)



# ----------------------------------------

def currying_func2(arg1, arg2, arg3):
    print('hello')
    def currying_func2(resolve, reject):
        print('arg1', arg1)
        print('arg2', arg2)
        print('arg3', arg3)
        resolve('Bye!')
    return Promise(currying_func2)

currying_func2 = curry(currying_func2)
currying_func2(1)(2)(3).then(print)

# -----------------------------------------

def promise_curried_func(resolve, reject, arg3):
    print(resolve, reject, arg3)

promise_curried_func = curry(promise_curried_func)

promise_curried_func = promise_curried_func(Promise(lambda resolve, reject: promise_curried_func(resolve, reject)))


# promise_curried_func = promise_curried_func(1)(2)(3)

# -----------------------------------------

# This does not work

# def currying_func2(arg1, arg2, arg3):
#     print(arg1)
#     print(arg2)
#     print(arg3)

# curry(currying_func2)

# print(currying_func2)