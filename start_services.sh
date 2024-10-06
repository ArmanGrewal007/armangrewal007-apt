#! /usr/bin/env zsh 
# falls back to bash if not found

###### THIS SCRIPT IS TO BE RUN ON MACHINE WHERE DOCKER IS INSTALLED ######

# Pull the images if they are not present
docker pull --platform linux/amd64 ubuntu:latest || true
docker tag ubuntu:latest ubuntu:amd64 || true

docker pull --platform linux/arm64 ubuntu:latest || true
docker tag ubuntu:latest ubuntu:arm64 || true

# Start the services defined in docker-compose.yml
docker-compose up -d
