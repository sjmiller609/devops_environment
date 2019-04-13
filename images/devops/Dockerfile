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
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

# Setup up Ruby repository
RUN apt-add-repository ppa:brightbox/ruby-ng

# Update since we just installed repos
# Install apt pacakges
RUN apt-get update && apt-get install -y \
    man \
    iputils-ping \
    software-properties-common \
    build-essential libssl-dev libffi-dev \
    libxml2-dev libxslt1-dev \
    python-dev python-pip python-virtualenv \
    vim git nmap dtrx tree wget tmux net-tools groff less \
    ruby2.5 ruby2.5-dev \
    docker-ce \
    links

# Upgrade pip
RUN pip install --upgrade pip setuptools
# Install pip modules
RUN pip install boto boto3 awscli ansible testinfra requests cfn-flip twine cfn-man cookiecutter
# Set up tab completion for AWS CLI
RUN cp $(which aws_completer) /etc/bash_completion.d/aws_completer

# Install Chef Development Kit
RUN mkdir -p /opt/chefdkinstall && \
  cd /opt/chefdkinstall && \
  wget https://packages.chef.io/files/stable/chefdk/3.1.0/ubuntu/18.04/chefdk_3.1.0-1_amd64.deb && \
  dpkg -i /opt/chefdkinstall/chefdk_3.1.0-1_amd64.deb

# Install chef gems
RUN chef gem install kitchen-sync kitchen-ec2 kitchen-docker kitchen-dokken

# Style tmux
RUN cd /root && git clone --depth=1 https://github.com/gpakosz/.tmux.git && \
  ln -s -f /root/.tmux/.tmux.conf && \
  cp /root/.tmux/.tmux.conf.local /root

# Style terminal
RUN git clone --depth=1 https://github.com/Bash-it/bash-it.git /root/.bash_it && \
  /root/.bash_it/install.sh --silent --no-modify-config
COPY bashrc /root/.bashrc

# Configure vim
COPY vimrc /root/.vimrc
RUN mkdir -p /root/.vim/bundle && \
  git clone https://github.com/VundleVim/Vundle.vim.git /root/.vim/bundle/Vundle.vim && \
  vim -c 'PluginInstall' -c 'qa!'

# install terraform
RUN mkdir /opt/terraform_install && cd /opt/terraform_install && \
      wget https://releases.hashicorp.com/terraform/0.11.13/terraform_0.11.13_linux_amd64.zip && \
      unzip terraform_0.11.13_linux_amd64.zip && \
      mv terraform /usr/local/bin/

WORKDIR /root/shared
