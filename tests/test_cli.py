#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `devops_environment` package."""

import os
os.environ['LC_ALL'] = 'C.UTF-8'
os.environ['LANG'] = 'C.UTF-8'

import pytest

from click.testing import CliRunner

from devops_environment import devops_environment
from devops_environment import cli

def test_cli_help():
    """Test the CLI --help flag"""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0, \
        "Expected exit_code 0, but got "+ str(help_result.exit_code) +\
        "\n" + str(help_result.output)
    assert '--help  Show this message and exit.' in help_result.output
