from rx import Observer
from with_class import create_observable

class PrintObserver(Observer):

    def on_next(self, value):
        print("Received {0}".format(value))

    def on_completed(self):
        print("Done!")

    def on_error(self, error):
        print("Error Occurred: {0}".format(error))

# This does not work
# def PrintObserver(Observer):

#     def on_next(value):
#         print("Received {0}".format(value))

#     def on_completed():
#         print("Done!")

#     def on_error(self, error):
#         print("Error Occurred: {0}".format(error))

# def 

# push_five_things = PushFiveThings()
# source = Observable.create(push_five_things.set_observer)
# source.subscribe(PrintObserver())
# push_five_things.send_value('some value')

source, observable = create_observable()
print('source', source)
# This is for using with def PrintObserver
# source.subscribe(PrintObserver(Observer))
source.subscribe(PrintObserver())
observable.send_value(1)