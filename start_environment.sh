#!/bin/bash

# DIR is set to the directory of this bash script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

docker build -t devops_kitchen_sink $DIR
if [ ! $? -eq 0 ]; then
  echo 'build failed'
  exit 1
fi
if [ ! -d $HOME/.ssh ]; then
  mkdir $HOME/.ssh
fi
if [ ! -d $DIR/backup ]; then
  mkdir $DIR/backup
fi
docker run -it --rm \
  --privileged \
  --network=host \
  -v $HOME/.gitconfig:/root/.gitconfig \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v $HOME/.ssh/:/root/.ssh/ \
  -v $DIR/backup:/root/backup \
  -v $DIR/sample_chef:/root/samples/sample_chef \
  devops_kitchen_sink /bin/bash
