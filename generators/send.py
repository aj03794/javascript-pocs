def echo(value=None):
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                value = (yield value)
            except Exception as e:
                value = e
    finally:
        print("Don't forget to clean up when 'close()' is called.")

generator = echo(1)
print(next(generator))


# print(next(generator))

print(generator.send(2))
# print(next(generator))
generator.send(3)
# print(next(generator))

generator.throw(TypeError, "spam")

generator.close()