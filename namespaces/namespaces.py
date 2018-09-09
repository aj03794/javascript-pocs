glob = 1

def foo():
    loc = 5
    print('loc i foo():', 'loc' in locals())

foo()
print('loc in global:', 'loc' in globals())
print('glob in global:', 'foo' in globals())

# loc i foo(): True
# loc in global: False
# glob in global: True

print(globals()) # prints global namespace

# {'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x10a6e3358>,
# '__spec__': None, '__annotations__': {}, '__builtins__':<module 'builtins' (built-in)>,
# '__file__': 'namespaces.py', '__cached__': None, 'glob': 1,
# 'foo': <function foo at 0x10a66af28>}

print(locals()) # prints local namespace

# {'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x10a6e3358>,
# '__spec__': None, '__annotations__': {}, '__builtins__':<module 'builtins' (built-in)>,
# '__file__': 'namespaces.py', '__cached__': None, 'glob': 1,
# 'foo': <function foo at 0x10a66af28>}
