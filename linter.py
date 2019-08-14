#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Denis Krienbühl
# Copyright (c) 2018 Denis Krienbühl
#
# License: MIT
#

"""This module exports the PuppetLint plugin class."""

from SublimeLinter.lint import Linter, util


class PuppetLint(Linter):
    """Provides an interface to puppet-lint."""

    defaults = {
        'selector': 'source.puppet'
    }
    cmd = ('puppet-lint', '--log-format', '%{line}:%{column}:%{kind}:%{message}', '*')

    regex = (
        r'^(?P<line>\d+):(?P<col>\d+):'
        r'((?P<warning>warning)|(?P<error>error)):'
        r'(?P<message>.+)'
    )
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH
    word_re = None
