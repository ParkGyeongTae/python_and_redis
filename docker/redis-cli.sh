#!/bin/bash

source .env
source redis.env

docker exec -it ${REDIS_CONTAINER_NAME} redis-cli -h 127.0.0.1 -p 6379 -a ${REDIS_PASSWORD}
