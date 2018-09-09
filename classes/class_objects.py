class MyClass:
    """ A simple example class """
    i = 12345
    def f(self):
        return 'hello world'

x = MyClass()

# Binding f to another variable without immediately invoking it
xf = x.f

print(x.i)
# 12345
# i is an integer object

# x.f is a function object

print(xf())