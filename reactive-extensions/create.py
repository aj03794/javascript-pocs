from rx import Observable

def subscribe(observer):

    observer.on_next('hello')

    def expose_funcs():
         def on_next(x):
            return x
            
        # def on_error(e):
        #     return e
        #     print("Got error: %s" % e)
                
        # def on_completed():
        #     print("Sequence completed")

        return on_next


    
    # return 1
    # return {
    #     'handleIncomingMessage': lambda (msg): observer.on_next(msg)
    # }




y = Observable.create(subscribe)



print('y', y)

# observer.on_next(3)

# y.subscribe(lambda msg: print('msg', msg))


# ----------------------------------


# def some_api_route(observer):

#     def on_next(x):
#         print('x', x)
#         return x
            
#     def on_error(e):
#         return e
#         print("Got error: %s" % e)

#     observer.on_next(1)
            
#     def on_completed():
#         print("Sequence completed")
    

# a = Observable.create(some_api_route)
# a.subscribe(print)