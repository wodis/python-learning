# encoding: utf-8
__author__ = 'wudi'

import demjson

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

json = demjson.encode(data)
print json

json = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
text = demjson.decode(json)
print  text