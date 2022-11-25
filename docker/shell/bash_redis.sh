#!/bin/bash

source .env

docker exec -it ${REDIS_CONTAINER_NAME} bash