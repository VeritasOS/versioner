# -*- coding: utf-8 -*-

from .manager import (
    NPM, DEP, GenericTOML, GenericYAML
)

# Supported list of package managers
PACKAGE_MANAGERS = {
    'npm': NPM,
    'dep': DEP,
    'yaml': GenericYAML,
    'toml': GenericTOML,
}


class Versioner(object):

    def __init__(self, package_manager):
        self.package_manager = package_manager

    def read(self, file, key_depth):
        manager = PACKAGE_MANAGERS.get(self.package_manager)
        if not manager:
            raise Exception("Supported package managers {0}".format(PACKAGE_MANAGERS.keys()))
        return manager().read(file, key_depth)
