#!/bin/bash

docker run -it --rm postgres:13 psql -h `ifconfig en0 | awk '/inet /{print $2}'`
