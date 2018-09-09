a = 5
b = 6
c = 10
for i in range(n):
    for j in range(n):
        x = i * i
        y = j * j
        z = i * j
for k in range(n):
    w = a * k + 45
    v = b * b
d = 33

# The number of assingment operations is the sum of 4 terms

# The first term is the constant `3` representing the 3 assignment statements at the start
# The second term is 3n^2 since there are 3 statements that are preformed n^2 times due
# to the nest iteration

# The 3rd term is 2n, two statements being iterated `n` times

#  Finally, the 4th term is the constant 1, representing the final assignment statement

# This gives us T(n)= 3 + 3n^2 + 2n + 1 = 3n^2 + 2n + 4

# Big O for this problem would be n^2