# -*- coding: utf-8 -*-

from .parser import (
    YAMLParser, TOMLParser, JSONParser
)


class NPM(JSONParser):
    # Default config file
    FILE = "package.json"

    # Path till version
    VERSION = ["version"]


class DEP(TOMLParser):
    # Default config file
    FILE = "Gopkg.toml"

    # Path till version
    VERSION = ["metadata", "version"]


class GenericTOML(TOMLParser):
    # Default config file
    FILE = ""

    # Path till version
    VERSION = []


class GenericYAML(YAMLParser):
    # Default config file
    FILE = ""

    # Path till version
    VERSION = []


class GenericJSON(JSONParser):
    # Default config file
    FILE = ""

    # Path till version
    VERSION = []
