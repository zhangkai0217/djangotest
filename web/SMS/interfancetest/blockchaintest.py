import json

import requests

url = 'https://portal.gotrack.com.cn/api/provenance-node-info/'
s = json.dumps({'label': 'beadb3-1590477575-416908'})
r = requests.post(url, data=s, headers={'content-type': 'application/json'})
print(r.text)
