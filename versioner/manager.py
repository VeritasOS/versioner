# -*- coding: utf-8 -*-

from .parser import (
    YAMLParser, TOMLParser
)


class NPM(YAMLParser):
    # Default config file
    FILE = "package.json"

    # Path till version
    VERSION = ["version"]


class DEP(TOMLParser):
    # Default config file
    FILE = "Gopkg.toml"

    # Path till version
    VERSION = ["metadata", "version"]
