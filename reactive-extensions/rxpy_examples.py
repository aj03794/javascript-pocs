from rx import Observable, Observer



# class PushFiveThings:

#     def __init__(self):
#         self.observer = None
        
#     @property
#     def observer(self):
#         return self.observer

#     @observer.setter
#     def observer(self, value):
#         self.observer = value
        # print('--->', self.__dict__)
        # self._observer.on_next('hello')

def PushFiveThings():

    def set_observer(observer):
        print('observer', observer)
        nonlocal internal_observer
        internal_observer = observer
        # internal_observer.on_next('hello there')

    def on_next(value):
        nonlocal internal_observer
        print('internal_observer', internal_observer)
        # internal_observer.on_next(value)
    
    internal_observer = 'Nothing'
    # set_observer('some over thing')
    # print('internal_observer', internal_observer)
    # on_next('some other value')

    return (set_observer, on_next)
    

class PrintObserver(Observer):

    def on_next(self, value):
        print("Received {0}".format(value))

    def on_completed(self):
        print("Done!")

    def on_error(self, error):
        print("Error Occurred: {0}".format(error))

set_observer, on_next = PushFiveThings()
source = Observable.create(set_observer)
# THIS DOES NOT WORK FOR SOME REASON
# INTERNAL OBSERVER DOES NOT GET SET UNTIL IT IS SUBSCRIBED TO
# on_next('next hello')
source.subscribe(PrintObserver())
on_next('next hello')
