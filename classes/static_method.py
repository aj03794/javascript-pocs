class SomeClass:

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def get_arg1(self):
        return self.arg1
    
    def get_arg2(self):
        return self.arg2

    @staticmethod
    def return_arg(arg):
        return arg


print(SomeClass.return_arg(1))
# 1