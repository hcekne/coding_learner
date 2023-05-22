#!/bin/bash

# get the image ID of the container named b2b_scorer_engine #--no-cache 

IMAGE_ID=$(docker images --filter=reference=b2b_scorer_engine --format "{{.ID}}")

docker build -t b2b_scorer_engine . 

docker rmi $IMAGE_ID
