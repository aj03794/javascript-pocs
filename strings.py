# String reversal
a = 'abcdefghijklmnopqrstuvwxyz'

# Reverse the list
print(a[::-1])

# Skip 2
print(a[::2])
# yxwvutsrqponmlkjihgfedcba
# acegikmoqsuwy

chars = []
for char in reversed(a):
    chars.append(char)

print('chars - 1', ''.join(str(char) for char in chars))
print('chars - 2', ''.join(map(str, chars)))

# chars - 1 zyxwvutsrqponmlkjihgfedcba
# chars - 2 zyxwvutsrqponmlkjihgfedcba

print('map(str, chars))', ' '.join(map(str, chars)))

# z y x w v u t s r q p o n m l k j i h g fe d c b a

num = 123456789
print(int(str(num)[::-1]))


# -----------------------------------------

a = 'abcdefghijklmnopqrstuvwxyz'
# This just makes a copy
print(a[:-1])
# abcdefghijklmnopqrstuvwxy
