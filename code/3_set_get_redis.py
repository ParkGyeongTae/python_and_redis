import os
import redis

if os.environ.get('redis_host') == None:
    os.environ['redis_host'] = 'redis'
if os.environ.get('redis_port') == None:
    os.environ['redis_port'] = '6379'

env_dict = {}

for key, value in os.environ.items():
    env_dict.setdefault(key, value)

redis_host = env_dict['redis_host']
redis_port = env_dict['redis_port']

redis_client = redis.StrictRedis(host = redis_host, port = redis_port, db = 0, password = 'password')

redis_client.set('1', '2')
redis_client.set('3', '4')

print(redis_client.get('1'))
print(redis_client.get('3'))

# redis_client.flushall()