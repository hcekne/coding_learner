#!/bin/bash

# script to run docker container to host the flaks scorer app

docker run -it --rm --expose 5000 -p 5000:5000 -v "$(pwd)":/python-docker/  b2b_scorer_engine