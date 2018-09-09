from rx import Observable, Observer

print('Observer', Observer)

# source = Observable.from_list([1,2,3,4,5,6])
# source.subscribe(print)
# 1
# 2
# 3
# 4
# 5
# 6

# --------------------------

# def on_next(x):
#         print("Got: %s" % x)
        
# def on_error(e):
#         print("Got error: %s" % e)
        
# def on_completed():
#         print("Sequence completed")

# xs = Observable.from_iterable(range(10))
# d = xs.subscribe(on_next, on_error, on_completed)


# -----------------------------

class MyObserver():

    def on_next(self, x):
        print("Got: %s" % x)
        
    def on_error(self, e):
        print("Got error: %s" % e)
        
    def on_completed(self):
        print("Sequence completed")

# xs = Observable.from_iterable(range(10))
# d = xs.subscribe(MyObserver())

# ------------------------------

# def my_observer():

#     def on_next(x):
#             print("Got: %s" % x)
            
#     def on_error(e):
#             print("Got error: %s" % e)
            
#     def on_completed():
#             print("Sequence completed")
    
#     return ( on_next, on_error, on_completed )

# ( on_next, on_error, on_completed ) = my_observer()


# xs = Observable.from_iterable(range(10))

# print('xs', xs)

# xs.from_iterable([123412])

# d = xs.subscribe(on_next, on_error, on_completed)



# -------------------------------

# x = Observable.interval(1000) \
#     .map(lambda i: "{0} Mississippi".format(i)) \
#     # .subscribe(lambda s: print(s))

# x.subscribe(lambda s: print(s))

# input("Press any key to quit\n")



# --------------------------------

# def subscribe(something):

#     def on_next(x):
#         return x
            
#     def on_error(e):
#         return e
#         print("Got error: %s" % e)
            
#     def on_completed():
#         print("Sequence completed")

#     something.on_next('hello')
    
#     # return 1
#     return ( on_next, on_error )


# y = Observable.create(subscribe)


# print('y', y)

# # observer.on_next(3)

# y.subscribe(lambda msg: print('msg', msg))


# --------------------------------

# def on_next(x):
#     print('x', x)
#     return x
        
# def on_error(e):
#     return e
#     print("Got error: %s" % e)
        
# def on_completed():
#     print("Sequence completed")

# xs = Observable.from_iterable(range(10))

# on_next(34244)

# my_observer = ( on_next, on_error, on_completed )

# o = xs.subscribe(on_next, on_error, on_completed)


# ----------------------------------