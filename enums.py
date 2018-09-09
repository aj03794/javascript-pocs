from enum import Enum

class Fruit(Enum):

    Apple = 0
    Pear = 1
    Banana = 2

print(type(Fruit))
# <class 'enum.EnumMeta'>
print(Fruit['Apple'], Fruit['Banana'])
# Output: Fruit.Apple, Fruit.Banana
print(Fruit['Apple'].value, Fruit['Banana'].value)
# Output: 0 2
print(Fruit.Apple.value)
# 0