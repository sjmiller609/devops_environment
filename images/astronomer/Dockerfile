# Steven Miller

FROM sjmiller609/env_base

# Install pip modules
RUN sudo pip3 install boto boto3 awscli ansible testinfra requests cfn-flip twine cfn-man cookiecutter pre-commit

# Set up tab completion for AWS CLI
RUN sudo cp $(which aws_completer) /etc/bash_completion.d/aws_completer

ARG TERRAFORM_VERSION=0.12.2

# Install terraform
RUN sudo mkdir /opt/terraform_install && cd /opt/terraform_install && \
      sudo wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
      sudo unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
      sudo mv terraform /usr/local/bin/

# Install kubectl
RUN cd /usr/local/bin && \
    sudo curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.12.0/bin/linux/amd64/kubectl && \
    sudo chmod +x ./kubectl

# Install aws-iam-authenticator
RUN cd /usr/local/bin && \
      sudo curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.12.7/2019-03-27/bin/linux/amd64/aws-iam-authenticator && \
      sudo chmod +x aws-iam-authenticator

# Install Helm
RUN sudo curl https://raw.githubusercontent.com/helm/helm/master/scripts/get | /bin/bash

# install gcloud
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - && sudo apt-get update && sudo apt-get install -y google-cloud-sdk

COPY gssh /usr/bin/gssh
