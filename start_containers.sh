#!/bin/bash

# Create a Docker network
NETWORK_NAME="ping_network"
docker network create $NETWORK_NAME

# Build Docker images
IMAGE1_NAME="container1"
IMAGE2_NAME="container2"
docker build -t $IMAGE1_NAME -f Dockerfile1 .
docker build -t $IMAGE2_NAME -f Dockerfile2 .

# Run the containers
CONTAINER1_NAME="container1"
CONTAINER2_NAME="container2"
docker run -d --name $CONTAINER1_NAME --network $NETWORK_NAME $IMAGE1_NAME
docker run -d --name $CONTAINER2_NAME --network $NETWORK_NAME $IMAGE2_NAME 