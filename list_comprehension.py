squares = []

print('range(10)', range(10))

# range(10) gives values 0 - 9
for x in range(10):
    print('x', x)
    squares.append(x**2)

print('squares', squares)


# ------------------------------

squares_two = list(map(lambda x: x**2, range(10)))
print('squares_two', squares_two)

# ------------------------------

squares_three = [x**2 for x in range(10)]
print('squares_three', squares_three)

# ------------------------------

def some_func(x):
    return x**2

squares_four = [some_func(x) for x in range(10)]
print('squares_four', squares_four)




# ---------------------------------

def a(num, elem):
    print('num', num)
    print('elem', elem)
    return num

vec = [[1,2,3], [4,5,6], [7,8,9]]
changed_vec = [a(num, elem) for elem in vec for num in elem]
print('changed_vec', changed_vec)

# num 1
# elem [1, 2, 3]
# num 2
# elem [1, 2, 3]
# num 3
# elem [1, 2, 3]
# num 4
# elem [4, 5, 6]
# num 5
# elem [4, 5, 6]
# num 6
# elem [4, 5, 6]
# num 7
# elem [7, 8, 9]
# num 8
# elem [7, 8, 9]
# num 9
# elem [7, 8, 9]
# changed_vec [1, 2, 3, 4, 5, 6, 7, 8, 9]

