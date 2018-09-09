from abc import ABC, abstractmethod

class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        print('Some implementation')

class AnotherSubclass(AbstractClassExample):

    def do_something(self):
        super().do_something()
        print('The enrichment from AnotherSubclass')

x = AnotherSubclass()
x.do_something()
# Some implementation
# The enrichment from AnotherSubclass


def main_func():

    def do_something():
        print('main func do something')
    
    return do_something


def another_func():
    do_something = main_func()
    do_something()


another_func()