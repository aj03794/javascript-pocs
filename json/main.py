import json
import os

print(os.getcwd())

# This did not work with just 'example.json'
f = open('/Users/axj1l59/Desktop/python-pocs/json/example.json', 'r')

json_data = f.read()
data = json.loads(json_data)

print('data', data)
print('data', data['some'])
# data {'some': 'data'}
# data data

f.close()