from rx import Observable

def some_func():
    return 1


observer = Observable.start(some_func)

observer.subscribe(print)