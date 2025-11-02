#!/bin/bash
set -e

mongoimport \
    --db restaurants \
    --collection restaurants \
    --file /tmp/restaurants.jsonl \
    --type json \
    -u $MONGO_INITDB_ROOT_USERNAME \
    -p $MONGO_INITDB_ROOT_PASSWORD \
    --authenticationDatabase admin