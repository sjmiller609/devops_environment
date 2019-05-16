# -*- coding: utf-8 -*-
"""Main module."""

import os
import docker

home = os.environ.get("HOME")
if not home:
    home = "."
home = os.path.realpath(home)


def idempotent_make_backup_folder(directory=None):
    if not directory:
        directory = os.environ['HOME'] + "/development_backup"
    if not os.path.isdir(directory):
        print("Creating backup directory " + directory)
        os.mkdir(directory)
    else:
        print("Using existing backup directory " + directory)


def pull_image(image='sjmiller609/env_astronomer', version="latest"):
    docker_client = docker.from_env()
    print("Pulling image " + image + ":" + version)
    docker_client.images.pull(image, tag=version)
    print("Done pulling image.")


def _get_mount_if_present(mounts):
    mount_command = ""
    for mount in mounts:
        if os.path.isfile(mount) or os.path.isdir(mount) or os.path.islink(mount):
            mount_command += "-v " + mount + ":" + mount.replace(home, '/root').replace("~",'/root') + " "
    return mount_command.strip()


def print_run_command():
    mounts = [
        "{}/.gitconfig".format(home),
        "{}/.ssh".format(home),
        "/var/run/docker.sock"
    ]
    mount_commands = _get_mount_if_present(mounts)

    print("""
    docker run -it --rm {mount_commands}
      -v {home}/development_backup:/root/shared \
      sjmiller609/env_astronomer /bin/bash
    """.format(mount_commands=mount_commands, home=home))


def setup():
    pull_image()
    idempotent_make_backup_folder()
    return 0
