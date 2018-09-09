from rx import Observable, Observer

# class ObservableCreator:

#     def __init__(self):
#         self.observer = None

#     def set_observer(self, observer):
#         self.observer = observer

#     def send_value(self, value):
#         self.observer.on_next(value)
    

# def create_observable():
#     observable = ObservableCreator()
#     source = Observable.create(observable.set_observer)
#     print('hello')
#     return source, observable
# class PrintObserver(Observer):

#     def on_next(self, value):
#         print("Received {0}".format(value))

#     def on_completed(self):
#         print("Done!")

#     def on_error(self, error):
#         print("Error Occurred: {0}".format(error))

# push_five_things = PushFiveThings()
# source = Observable.create(push_five_things.set_observer)
# !!!!!!! IMPORTANT !!!!!!!
# THIS DOES NOT WORK FOR SOME REASON
# INTERNAL OBSERVER DOES NOT GET SET UNTIL IT IS SUBSCRIBED TO
# on_next('next hello')
# source.subscribe(PrintObserver())
# push_five_things.send_value('some value')

# ---------------------------------------

def observable_creator(observer):
    
    def send_value(value):
        observer.on_next(value)
    
    return send_value

source = Observable.create(observable_creator)
source.subscribe(on_next=lambda value: print("{0}".format(value)),
                on_completed=lambda: print("Completed"),
                on_error=lambda e: print(e))
