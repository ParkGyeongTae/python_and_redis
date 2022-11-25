#!/bin/bash

source `dirname "$0"`/../.env

docker exec -it ${PYTHON_CONTAINER_NAME} bash