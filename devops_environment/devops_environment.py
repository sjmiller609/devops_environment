# -*- coding: utf-8 -*-

"""Main module."""

import os
import sys
import docker

home = os.environ.get("HOME")
if not home:
    home = "."

def idempotent_make_backup_folder(directory=None):
    if not directory:
        directory = os.environ['HOME'] + "/development_backup"
    if not os.path.isdir(directory):
        print("Creating backup directory " + directory)
        os.mkdir(directory)
    else:
        print("Using existing backup directory " + directory)

def pull_image(image='sjmiller609/stelligent_development', version="latest"):
    docker_client = docker.from_env()
    print("Pulling image " + image + ":" + version)
    docker_client.images.pull(image, tag=version)
    print("Done pulling image.")

def _get_mount_commands_for_directories(directories):

def print_run_command():
    directories = ["{}/.gitconfig".format(home),
                   "{}/.ssh".format(home),
                   "/var/run/docker.socket"]
    mount_commands = _get_mount_commands_for_directories(directories)

    if not os.path.isfile(mount_git_config):
        mount_git_config = ""
    else:
        mount_git_config = "-v " + mount_git_config

    mount_ssh_config = "{}/.ssh".format(home)
    if not os.path.isfile(mount_ssh_config):
        mount_ssh_config = ""
    else:
        mount_ssh_config = "-v " + mount_ssh_config

    mount_docker_socket = "/var/run/docker.sock"
    if not os.path.isfile(mount_docker_socket):
        mount_docker_socket = ""
    else:
        mount_docker_socket = "-v " + mount_docker_socket

    print("""
    docker run -it --rm {mount_commands}
      -v {home}/development_backup:/root/shared \
      sjmiller609/stelligent_development /bin/bash
    """.format(mount_commands=mount_commands, home=home))

def setup():
    pull_image()
    idempotent_make_backup_folder()
    return 0
