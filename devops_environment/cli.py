# -*- coding: utf-8 -*-

"""Console script for devops_environment."""
import sys
import click
import devops_environment


@click.command()
def main(args=None):
    """Console script for devops_environment."""
    return devops_environment.main()

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
