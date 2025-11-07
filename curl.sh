#!/bin/bash

curl --location 'localhost:8000/users' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "adrien",
    "email": "adrien@test.com"    
}'