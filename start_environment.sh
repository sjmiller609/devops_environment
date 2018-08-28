if [ ! -d $HOME/development_backup ]; then
  mkdir $HOME/development_backup
fi
docker run -it --rm \
  -v $HOME/.gitconfig:/root/.gitconfig \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v $HOME/.ssh/:/root/.ssh/ \
  -v $HOME/development_backup:/root/shared \
  sjmiller609/stelligent_development /bin/bash
