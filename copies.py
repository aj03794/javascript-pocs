a = [[1, 2], [3, 4]]
b = a[:]

print(a)
print(b)
print('a is b', a is b)

# [[1, 2], [3, 4]]
# [[1, 2], [3, 4]]
# a is b False

a[0] = [8, 9]

print('a', a)
print('b', b)

# a [[8, 9], [3, 4]]
# b [[1, 2], [3, 4]]

a[1].append(5)
print('a', a)
print('b', b)
# a [[8, 9], [3, 4, 5]]
# b [[1, 2], [3, 4, 5]]