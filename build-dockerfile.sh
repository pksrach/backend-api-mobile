#!/bin/bash

CONTAINER=backend-api-mobile
TAG=latest
IMAGE="pksrach/$CONTAINER:$TAG"

# Build the docker image
docker build -t $IMAGE .

# Push the docker image
docker push $IMAGE