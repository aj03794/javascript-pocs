import redis
import time

def my_handler(message):
    print ('MY HANDLER: ', message['data'])

r = redis.StrictRedis(host="localhost", port=6379, charset="utf-8", decode_responses=True)
p = r.pubsub(ignore_subscribe_messages=True)

p.subscribe(**{'my-channel': my_handler})
# read the subscribe confirmation message
# print(p.get_message())
# {'pattern': None, 'type': 'subscribe', 'channel': 'my-channel', 'data': 1L}
r.publish('my-channel', '1')
print('1', p.get_message())
r.publish('my-channel', '2')
print('2', p.get_message())
print('3', p.get_message())