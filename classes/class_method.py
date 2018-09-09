# This does not work
# class MyClass(number):

class MyClass(number):

    # print('some_param', some_param)

    def method(self):
        print('instance method called')
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        print('class method called')
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        print('static method called')
        return 'static method called'



# Does not work
# myClass = MyClass(1)

myClass = MyClass()

# myClass.method()
# myClass.classmethod()
# myClass.staticmethod()

# print('--------------------------------')

# # Can also do
# MyClass.method(myClass)

# # Works
# print('--------------------------------')
# MyClass.staticmethod()
# MyClass.classmethod()
# # Fails
# MyClass.method()

# Class methods
# Because the class method only has access to this cls argument,
# it can’t modify object instance state

# Instance methods
# Can access instance state through the 