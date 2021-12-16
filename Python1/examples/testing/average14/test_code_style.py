"""Implementace jednotkových testů."""

from pathlib import Path
from sys import exit
import pycodestyle
import pytest

from average import average


def test_code_style():
    files = list(Path(".").rglob("*.py"))

    style = pycodestyle.StyleGuide(quiet=False, config_file="setup.cfg")
    result = style.check_files(files)
    print("Total errors:", result.total_errors)
    assert result.total_errors == 0, "Detected {} code style problems".format(
        result.total_errors
    )
