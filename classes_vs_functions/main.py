from types import SimpleNamespace
import enum

class SomeClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def get_arg1(self):
        return self.arg1
    
    def get_arg2(self):
        return self.arg2


class_instance = SomeClass('arg1', 'arg2')
# Doing this lists everything on the class in a list
# print('class_instance', dir(class_instance))
class_instance.get_arg1()
class_instance.get_arg2()
# get_arg1 called
# get_arg2 called


# --------------------------------------------

class Fruit(enum.Enum):
    Apple = 0
    Pear = 1
    Banana = 2

print(Fruit['Apple'], Fruit['Banana'])
# Output: Fruit.Apple, Fruit.Banana
print(Fruit['Apple'].value, Fruit['Banana'].value)
print(Fruit.Apple.value)
# Output: 0 2

# --------------------------------------------

def some_func(arg1, arg2):

    def get_arg1():
        return arg1
    
    def get_arg2():
        return arg2

    
    to_return = {
        'get_arg1': lambda: get_arg1(),
        'get_arg2': lambda: get_arg2()
    }

    return to_return

func_instance = some_func('arg1', 'arg2')
print(func_instance['get_arg1']())
print(func_instance['get_arg2']())
# some_func get_arg1 called
# arg1
# some_func get_arg2 called
# arg2

# --------------------------------------------

def some_func2(arg1, arg2):

    def get_arg1():
        print('some_func get_arg1 called')
        return arg1
    
    def get_arg2():
        print('some_func get_arg2 called')
        return arg2

    
    to_return = SimpleNamespace(**{
        'get_arg1': lambda: get_arg1(),
        'get_arg2': lambda: get_arg2()
    })

    return to_return

func_instance2 = some_func2('arg1', 'arg2')
print(func_instance2.get_arg1())
print(func_instance2.get_arg2())
