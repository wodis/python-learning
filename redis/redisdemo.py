__author__ = 'wudi'

import redis

pool = redis.ConnectionPool(host='172.16.2.169', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

r.set('bing', 'baz')
bing = r.get('bing')

print bing

ran = r.keys('feed_rank_*')

for cur in ran:
    print cur