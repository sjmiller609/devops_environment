# kitchen-sink for devops development environment
# Steven Miller

FROM ubuntu:18.04

# Do not exclude man pages & other documentation
RUN rm /etc/dpkg/dpkg.cfg.d/excludes
# Reinstall all currently installed packages in order to get the man pages back
RUN apt-get update && \
    dpkg -l | grep ^ii | cut -d' ' -f3 | xargs apt-get install -y --reinstall && \
    rm -r /var/lib/apt/lists/*
    
# Install core
# software-properties-common is necessary for "add-apt-repository"
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common \
    build-essential libssl-dev libffi-dev

# Set up Docker repository
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

# Setup up Ruby repository
RUN apt-add-repository ppa:brightbox/ruby-ng

# Update since we just installed repos
RUN apt-get update

# Install Docker
RUN apt-get install -y docker-ce

# Install Python
RUN apt-get install -y \
    python-dev python-pip python-virtualenv
# upgrade pip
RUN pip install --upgrade pip setuptools
# install ansible
RUN pip install ansible

# Install Ruby
RUN apt-get install -y ruby2.5 ruby2.5-dev

# Install general development tools
RUN apt-get install -y \
    vim git nmap dtrx tree wget tmux net-tools

# Install Amazon Web Services Command Line Interface
RUN pip install boto boto3 awscli

# Install Cago - helps manage AWS credentials
RUN mkdir -p /opt/cagoinstall
RUN cd /opt/cagoinstall && wget https://github.com/electric-it/cagophilist/releases/download/v2.3.1/cago-linux-amd64-v2.3.1.tar.gz
RUN cd /opt/cagoinstall && dtrx /opt/cagoinstall/cago-linux-amd64-v2.3.1.tar.gz
RUN cp /opt/cagoinstall/cago-linux-amd64-v2.3.1.tar.gz /usr/local/bin

# Install Chef Development Kit
RUN mkdir -p /opt/chefdkinstall
RUN cd /opt/chefdkinstall && wget https://packages.chef.io/files/stable/chefdk/3.1.0/ubuntu/18.04/chefdk_3.1.0-1_amd64.deb
RUN dpkg -i /opt/chefdkinstall/chefdk_3.1.0-1_amd64.deb

RUN chef gem install kitchen-sync kitchen-ec2 kitchen-docker kitchen-dokken

# Style terminal
RUN git clone --depth=1 https://github.com/Bash-it/bash-it.git /root/.bash_it
RUN /root/.bash_it/install.sh --silent --no-modify-config
COPY bashrc /root/.bashrc
# Style vim
COPY vimrc /root/.vimrc
# Style tmux
RUN cd /root && git clone --depth=1 https://github.com/gpakosz/.tmux.git
RUN ln -s -f /root/.tmux/.tmux.conf
RUN cp /root/.tmux/.tmux.conf.local /root

WORKDIR /root

# copy sample chef repo
COPY sample_chef /root/samples/sample_chef

