from rx import Observable, Observer

def PushFiveThings():

    def set_observer(observer):
        nonlocal internal_observer
        internal_observer = observer

    def on_next(value):
        nonlocal internal_observer
        internal_observer.on_next(value)
    
    internal_observer = None

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
# INTERNAL OBSERVER DOES NOT GET SET UNTIL IT IS SUBSCRIBED TO (on 2nd line below)
# on_next('next hello')
source.subscribe(PrintObserver())
on_next('next hello')
