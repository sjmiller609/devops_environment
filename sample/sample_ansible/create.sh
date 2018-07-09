#!/bin/bash

if [ "$VAULT_PASS" = "" ]; then
	echo "VAULT_PASS must be provided as an environment varible. This password should have been provided by Steven."
	exit 1
fi
echo "$VAULT_PASS" > ~/ansible_vault_secret

# get the directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# provision the server
ansible-playbook $DIR/ansible/playbooks/provision.yml -i $DIR/ansible/inventory/provisioner.yml --vault-password-file ~/ansible_vault_secret

# ec2.py copy/pasted from amazon
# https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.py
ansible-playbook $DIR/ansible/playbooks/deploy.yml -i $DIR/ansible/inventory/demo.yml --vault-password-file ~/ansible_vault_secret


source /testenv/bin/activate
py.test --connection=ansible --ansible-inventory $DIR/ansible/inventory/demo.yml --hosts=webserver $DIR/tests/test_server.py
# using 'testinfra' pip module to make sure nginx is started and enabled
# and 200 with correct content when requested.
# python $DIR/tests/testinfra.py
