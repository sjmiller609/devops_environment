# -*- coding: utf-8 -*-
"""
Console script for devops_environment.

ARG_NAME:
    'setup' or 'print_run_command'

"""
import sys
import click
import devops_environment


@click.command()
@click.argument('arg_name')
def main(arg_name=None):
    """Console script for devops_environment."""
    if arg_name == "setup":
        return devops_environment.setup()
    elif arg_name == "print_run_command":
        return devops_environment.print_run_command()
    else:
        raise RuntimeError()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
