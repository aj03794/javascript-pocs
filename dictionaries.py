from types import SimpleNamespace



# Can use dot operator to access properties on a dictionary doing this, but can no longer access by index
d = SimpleNamespace(**{
    'key1': 'value1',
    'key2': 'value2'
})

# n = SimpleNamespace(**d)
# print('n', n)

print('d', d)
print('d.key1', d.key1)
# print('d[key1]', d['key1'])
print(type(d))

# d namespace(key1='value1', key2='value2')
# d.key1 value1
# <class 'types.SimpleNamespace'>

# ------------------------
