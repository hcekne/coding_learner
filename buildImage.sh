#!/bin/bash

# get the image ID of the container coding_learner_container #--no-cache 

IMAGE_ID=$(docker images --filter=reference=coding_learner --format "{{.ID}}")

docker build -t coding_learner . 

docker rmi $IMAGE_ID
