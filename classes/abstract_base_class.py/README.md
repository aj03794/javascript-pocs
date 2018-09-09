- Abstract classes are classes that contain one or more abstract methods
    * An abstract method is a method that is declared, but contains no implementation
- Abstract classes may not be instantiated, and require subclasses to provide implementations for the abstract methods
- Subclasses of an abstract class in Python are not required to implement abstract methods of the parent class

-----------------------------------------------

```
class AbstractClass:

    def do_something(self):
        pass

class B(AbstractClass):
    pass

a = AbstractClass()
b = B()
```

- This is not an abstract class b/c
we can instantiate an instance from AbstractClass
we are not required to implement do_something in the class definition of B

- This example implemented a case of simple inheritance which has nothing
to do with an abstract class

- Python on its own doesn't provide abstract clases
- Python comes wiht a module which provides the infrastructure for defining Abstract Base Classes (ABCs)
    * This module is called abc

-----------------------------------------------

- A class that is derived from an abstract class cannot be instantiated unless all of its abstract methods are overridden

```
class AbstractClassExample(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass

class DoAdd42(AbstractClassExample):
    def do_something(self):
        return self.value + 42
```

- The do_something function in the DoAdd42 class `overrides` the `do_something` function in its parent class (AbstractClassExample which inherits from `ABC`)

-----------------------------------------------

- You may think that abstract methods can't be implemented in the abstract base class
    * `This is wrong`
- An abstract method can have an implementation in the abstract class
- Even if they are implemented, designers of subclasses will be forced to override the implementation

- Like in other cases of `normal` inheritance, the abstract method can be invoked with `super()` call mechanism
- This makes it possible to provide some basic functionality in the abstract method, which can then be enriched by the subclass implementation