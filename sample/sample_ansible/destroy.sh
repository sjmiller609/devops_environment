#!/bin/bash

if [ "$VAULT_PASS" = "" ]; then
	echo "VAULT_PASS must be provided as an environment varible. This password should have been provided by Steven."
	exit 1
fi
echo "$VAULT_PASS" > ~/ansible_vault_secret

# get the directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

ansible-playbook $DIR/ansible/playbooks/destroy.yml -i $DIR/ansible/inventory/provisioner.yml --vault-password-file ~/ansible_vault_secret
