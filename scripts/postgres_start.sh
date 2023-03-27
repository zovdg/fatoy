#!/bin/bash

docker run \
    --name postgres \
    -e POSTGRES_USER=root \
    -e POSTGRES_PASSWORD=notpassword \
    -p 5432:5432 \
    -d postgres:13
