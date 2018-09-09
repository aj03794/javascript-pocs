# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
[x**2 for x in my_list]

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
y = (x**2 for x in my_list)
print('y', y)
print(next(y))
print(next(y))
print(next(y))
# print(next(y))
# print(next(y))
y.send(5)
print(next(y))
