import sys

from flow_client import cli


def test_cli() -> None:
    """test no args"""
    sys.argv = []
    cli.main()


def test_list() -> None:
    """test list flow"""
    sys.argv = ["cli.py", "-l"]
    cli.main()
