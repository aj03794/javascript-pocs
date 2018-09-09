def scope_test():
    def do_local():
        spam = 'local spam'
        return spam
    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'
        return spam
    def do_global():
        global spam
        spam = 'global spam'
        return spam
    spam = 'test spam'
    do_local()
    print('After local assignment:', spam)
    do_nonlocal()
    print('After nonlocal assignment: ', spam)
    do_global()
    print('After global assignment', spam)

scope_test()
print('In global scope', spam)

# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# NOTE THIS ONE
# After global assignment: nonlocal spam
# In global scope: global spam
# In global scope global spam

# Note how the local assignment (which is defautl) didn't change
# scope_test's binding of spam