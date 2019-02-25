# -*- coding: utf-8 -*-

"""Main module."""

import os
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

def print_run_command():
    print("""
    docker run -it --rm \
      -v {home}/.gitconfig:/root/.gitconfig \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v {home}/.ssh/:/root/.ssh/ \
      -v {home}/development_backup:/root/shared \
      sjmiller609/stelligent_development /bin/bash
    """.format(home=home))

def setup():
    pull_image()
    idempotent_make_backup_folder()
    return 0
