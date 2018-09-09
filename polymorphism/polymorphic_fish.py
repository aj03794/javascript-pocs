class Shark():
    def swim(self):
        print('The shark is swimming')
    
    def swim_backwards(self):
        print('The shark cannot swim backwards, but can sink backwards')
    
    def skeleton(self):
        print("The shark's skeleton is made of cartilage")


class Clownfish():
    def swim(self):
        print("The clownfish can swim backwards")
    
    def swim_backwards(self):
        print("The clownfish can swim backwards")
    
    def skeleton(self):
        print("The clownfish's skeleton is made of bone")

# Bth the `shark` and the `Clownfish` classes have 3 methods with same name
# swim
# swim_backwards
# skeleton

sammy = Shark()
# sammy.skeleton()

casey = Clownfish()
# casey.skeleton()

# Iterates through the `sammy` instantiation of the `Shark` class
# then iterates through the `casey` object of the `Clownfish` class

# for fish in (sammy, casey):
#     fish.swim()
#     fish.swim_backwards()
#     fish.skeleton()

# The shark is swimming
# The shark cannot swim backwards, but can sink backwards
# The shark's skeleton is made of cartilage
# The clownfish can swim backwards
# The clownfish can swim backwards
# The clownfish's skeleton is made of bone

def in_the_pacific(fish):
    fish.swim()

in_the_pacific(sammy)
in_the_pacific(casey)
# The shark is swimming
# The clownfish can swim backwards

# Even though we pass a random object `(fish)` into the `in_the_pacific()` function
# when defining it

# We're still able to use it effectively (the same essentially) for instantiations
# of the `Shark` and `Clownfish` classes

# The casey object called the swim() method defined in the Clownfish class
# The sammy object called the swim() method defined in the Shark class

# By allowing different objects to leverage functions and methods in similar
# ways through polymorphism
# This feature allows greater flexibility and extendability of your OO code