# encoding: utf-8
import json
import requests

# GET
payload = {'key1': 'value1', 'uid': 130}

r = requests.get('http://localhost:8080/reverse-wrm', params=payload)

print r.status_code

print r.encoding

print r.url

print r.text

# POST
url = 'http://localhost:8080/filter-sensitive-content'
payload = {'content': '微博新业务微人脉'}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)

print r.status_code

print r.encoding

print r.url

print r.text