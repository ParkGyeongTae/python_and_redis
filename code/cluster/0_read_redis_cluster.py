from rediscluster import RedisCluster
import os

class RedisSetting():

    def get_redis_info():

        if os.environ.get('REDIS_HOST') == None:
            os.environ['REDIS_HOST'] = 'redis_1'
        if os.environ.get('REDIS_PORT') == None:
            os.environ['REDIS_PORT'] = '6379'
        if os.environ.get('REDIS_PASSWORD') == None:
            os.environ['REDIS_PASSWORD'] = 'password'

        env_dict = {}

        for key, value in os.environ.items():
            env_dict.setdefault(key, value)

        redis_host = env_dict['REDIS_HOST']
        redis_port = env_dict['REDIS_PORT']
        redis_password = env_dict['REDIS_PASSWORD']

        return redis_host, redis_port, redis_password

if __name__ == '__main__':

    redis_host, redis_port, redis_password = RedisSetting.get_redis_info()

    redis_client = RedisCluster(
        startup_nodes = [dict(host = redis_host, port = redis_port)],
        password = redis_password,
        decode_responses = True, 
        skip_full_coverage_check = True)
    
    print(redis_client)
    exit()

    redis_client.set(1, 3)
    redis_client.expire(1, 5)
    print(redis_client.get(1))


# redis.StrictRedis(host = redis_host, port = redis_port, db = 0, password = redis_password)



# client = RedisCluster(
# startup_nodes=[dict(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'))],
# decode_responses=True, skip_full_coverage_check=True)