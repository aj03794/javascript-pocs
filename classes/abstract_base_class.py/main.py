from abc import ABC, abstractmethod

# class AbstractClass:

#     def do_something(self):
#         pass

# class B(AbstractClass):
#     pass

# a = AbstractClass()
# b = B()

# ---------------------------------------------

class AbstractClassExample(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass

# This doesn't work because we don't implement the do_something function
# class DoAdd42(AbstractClassExample):
#     pass
# x = DoAdd42(4)

# Traceback (most recent call last):
#   File "main.py", line 29, in <module>
#     x = DoAdd42(4)
# TypeError: Can't instantiate abstract class DoAdd42 with abstract methods do_something

class DoAdd42(AbstractClassExample):
    def do_something(self):
        return self.value + 42

class DoMul42(AbstractClassExample):
    def do_something(self):
        return self.value * 42

x = DoAdd42(10)
y = DoMul42(10)
print(x.do_something())
print(y.do_something())
# 52
# 420

# ---------------------------------------------

class AbstractClassExample2(ABC):

    @abstractmethod
    def do_something(self):
        print('Some implementation')

class AnotherSubclass(AbstractClassExample2):

    def do_something(self):
        super().do_something()
        print('The enrichment from AnotherSubclass')

x = AnotherSubclass()
x.do_something()
# Some implementation
# The enrichment from AnotherSubclass