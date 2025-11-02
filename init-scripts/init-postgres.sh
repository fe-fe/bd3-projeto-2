#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    
    -- 1. Create the table
    CREATE TABLE IF NOT EXISTS restaurants (
        id SERIAL PRIMARY KEY,
        document jsonb
    );

    \copy restaurants (document) FROM '/tmp/restaurants.jsonl'
EOSQL