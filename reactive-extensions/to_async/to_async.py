from rx import Observable

res = Observable.to_async(lambda x, y: print(x + y))
res(3, 4)
# res = Observable.to_async(lambda x, y: x + y, Scheduler.timeout)(4, 3)
# res = Observable.to_async(lambda x: log.debug(x),
#                                     Scheduler.timeout)('hello')

# -------------------------------------

res = Observable.to_async(lambda x, y: x + y)
res(3, 4).subscribe(print)
res(5, 6).subscribe(print)


# -------------------------------------

res = Observable.to_async(lambda x, y: x + y)
subscription_one = res(3, 4)
subscription_two = res(5, 6)
