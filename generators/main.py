# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

a = my_gen()
next(a)
next(a)
next(a)
# Traceback (most recent call last):
#   File "main.py", line 20, in <module>
#     next(a)
# StopIteration
# next(a)


# --------------------------------------------------

# A simple generator function
def my_gen():
    x = yield
    yield x * 2

a = my_gen()
a.send(4)
print(next(a))
# next(a)
# next(a)