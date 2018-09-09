from promise import Promise

def x(arg1):
    print('hello')
    def x(resolve, reject):
        print('arg1', arg1)
        resolve('Bye!')
    return Promise(x)
# x('1').then(print)


def y():
    print('hello')
    def y(resolve, reject):
        # print('bye')
        resolve('Bye!')
    return Promise(x)
# y().then(print)

def z():
    print('z hello')
    def z(resolve, reject):
        print('z bye')
        resolve('z bye!')
    return lambda: Promise(z)
# z()().then(print)

x('1').then(lambda result: print('result', result))