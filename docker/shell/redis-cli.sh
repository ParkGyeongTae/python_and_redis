#!/bin/bash

source `dirname "$0"`/../.env
source `dirname "$0"`/../redis_settings/redis.env

docker exec -it ${REDIS_CONTAINER_NAME} redis-cli -h 127.0.0.1 -p 6379 -a ${REDIS_PASSWORD}
