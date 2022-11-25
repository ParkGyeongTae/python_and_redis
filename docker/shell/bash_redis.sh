#!/bin/bash

source `dirname "$0"`/../.env

docker exec -it ${REDIS_CONTAINER_NAME} bash