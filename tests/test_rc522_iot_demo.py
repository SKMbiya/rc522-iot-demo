#!/usr/bin/env python

"""Tests for `rc522_iot_demo` package."""


import unittest
from click.testing import CliRunner

from rc522_iot_demo import rc522_iot_demo
from rc522_iot_demo import cli


class TestRc522_iot_demo(unittest.TestCase):
    """Tests for `rc522_iot_demo` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'rc522_iot_demo.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
