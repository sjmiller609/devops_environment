#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `devops_environment` package."""

import os
import pytest
import subprocess
import testinfra
from time import sleep

image = 'sjmiller609/env_astronomer'

# scope='session' uses the same container for all the tests;
# scope='function' uses a new container per test function.
@pytest.fixture(scope='session')
def host(request):
    # run a container
    docker_id = subprocess.check_output(
        ['docker', 'run', '-d', image, '/bin/sleep','300']).decode().strip()
    # return a testinfra connection to the container
    yield testinfra.get_host("docker://" + docker_id)
    # at the end of the test suite, destroy the container
    subprocess.check_call(['docker', 'rm', '-f', docker_id])

def test_vimrc(host):
    vim_file = host.file("/root/.vimrc")
    assert vim_file.contains("set")

def test_in_path(host):

    required_in_path = ['python3',
                        'pip',
                        'virtualenv',
                        'ansible',
                        'terraform',
                        'kubectl',
                        'aws-iam-authenticator',
                        'helm']

    for item in required_in_path:
        assert host.exists(item), "Expected to find " + item + " in path"
