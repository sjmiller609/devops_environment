#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `devops_environment` package."""

import os
import pytest
import subprocess
import testinfra
from time import sleep

image = 'testimage'

this_directory = os.path.dirname(os.path.realpath(__file__))
docker_path = os.path.join(
    this_directory,
    '..',
    'images',
    'devops'
)

# scope='session' uses the same container for all the tests;
# scope='function' uses a new container per test function.
@pytest.fixture(scope='session')
def host(request):
    # build local ./Dockerfile
    subprocess.check_call(['docker', 'build', '-t', image, docker_path])
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

    required_in_path = ['python',
                        'python2',
                        'python3',
                        'pip',
                        'virtualenv',
                        'ansible']

    for item in required_in_path:
        assert host.exists(item), "Expected to find " + item + " in path"
