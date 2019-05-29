# Steven Miller

FROM ubuntu:18.04

# Do not exclude man pages & other documentation
# Reinstall all currently installed packages in order to get the man pages back
RUN rm /etc/dpkg/dpkg.cfg.d/excludes && apt-get update && \
    dpkg -l | grep ^ii | cut -d' ' -f3 | xargs apt-get install -y --reinstall && \
    rm -r /var/lib/apt/lists/*
    
# prepare for "add-apt-repository" and use of "curl"
RUN apt-get update && apt-get install -y \
    software-properties-common \
    apt-transport-https \
    curl \
    ca-certificates

# Set up Docker repository
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
  add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Update since we just installed repos
# Install apt pacakges
RUN apt-get install -y \
    sudo \
    man \
    iputils-ping \
    software-properties-common \
    build-essential \
    vim git nmap dtrx tree wget tmux net-tools groff less \
    docker-ce \
    python3-pip && \
    pip3 install --upgrade pip setuptools virtualenv

ENV USER=developer
ENV HOME=/home/$USER
RUN useradd -m -d $HOME $USER && \
    mkdir -p /etc/sudoers.d && \
    echo "$USER ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USER

USER $USER

RUN cd && \
    git clone --depth=1 https://github.com/gpakosz/.tmux.git && \
    ln -s -f .tmux/.tmux.conf && \
    cp .tmux/.tmux.conf.local .

# Style terminal
RUN git clone --depth=1 https://github.com/Bash-it/bash-it.git $HOME/.bash_it && \
  $HOME/.bash_it/install.sh --silent --no-modify-config
COPY bashrc $HOME/.bashrc

# Configure vim
COPY vimrc $HOME/.vimrc
RUN mkdir -p $HOME/.vim/bundle && \
  git clone https://github.com/VundleVim/Vundle.vim.git $HOME/.vim/bundle/Vundle.vim && \
  vim -c 'PluginInstall' -c 'qa!'

WORKDIR $HOME/shared
