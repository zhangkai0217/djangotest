import json
import time

import requests

# url = 'http://13.231.115.79:10000/createindividualproduct'
# headers = {'Content-Type': 'application/json'}
# index = 16088088
# count = 0
#
# timestart = time.time();
# for i in range(50):
#     obje = {}
#     string = str(index+i)
#     obje['productId'] = string
#     obje['label'] = string
#     obje['blockchainId'] = string
#     s = json.dumps(obje)
#     r = requests.post(url, data=s, headers={'Content-Type': 'application/json'})
#     if r.status_code != 200:
#         count = count + 1
# timeend = time.time()
# print(count)
# print(timeend-timestart)


url = 'http://13.231.115.79:10000/createproduct'
headers = {'Content-Type': 'application/json'}
index = 31088988
param = {}
arr = []

timestart = time.time();
for i in range(500):
    obje = {}
    string = str(index + i)
    obje['productId'] = string
    obje['label'] = string
    obje['blockchainId'] = string
    arr.append(obje)
param['products'] = arr
s = json.dumps(param)
r = requests.post(url, data=s, headers={'Content-Type': 'application/json'})
timeend = time.time()
print(timeend - timestart)
