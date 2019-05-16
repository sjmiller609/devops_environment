# Steven Miller

FROM sjmiller609/env_base

# Install pip modules
RUN pip3 install boto boto3 awscli ansible testinfra requests cfn-flip twine cfn-man cookiecutter

# Set up tab completion for AWS CLI
RUN cp $(which aws_completer) /etc/bash_completion.d/aws_completer

# Install terraform
RUN mkdir /opt/terraform_install && cd /opt/terraform_install && \
      wget https://releases.hashicorp.com/terraform/0.11.13/terraform_0.11.13_linux_amd64.zip && \
      unzip terraform_0.11.13_linux_amd64.zip && \
      mv terraform /usr/local/bin/

# Install kubectl 1.12
RUN cd /usr/local/bin && \
    curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.12.0/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl

# Install aws-iam-authenticator
RUN cd /usr/local/bin && \
      curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.12.7/2019-03-27/bin/linux/amd64/aws-iam-authenticator && \
      chmod +x aws-iam-authenticator

# Install Helm
RUN curl https://raw.githubusercontent.com/helm/helm/master/scripts/get | /bin/bash
