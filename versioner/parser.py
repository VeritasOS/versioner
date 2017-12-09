# -*- coding: utf-8 -*-

import os
from ruamel.yaml import YAML
import toml


class Parser(object):

    def _load_file(self, file):
        """
        Check file existance and return file instance
        """
        path = os.path.abspath(file) if file else os.path.join(
            os.getcwd(), self.FILE)
        return open(path, 'r')

    def _get_version(self, version_hierarchy):
        return version_hierarchy if version_hierarchy else self.VERSION

    def get_version(self, config, path):
        for var in path:
            value = config[var]
            if type(value) == dict:
                if len(path[1:]) > 0:
                    return self.get_version(value, path[1:])
                else:
                    # if traverse path is empty
                    # return dict as it is
                    return value
            else:
                return value


class YAMLParser(Parser):

    def read(self, file, version_hierarchy):
        content = YAML(typ='safe').load(
            self._load_file(file))
        return self.get_version(content,
            self._get_version(version_hierarchy))


class TOMLParser(Parser):

    def read(self, file, version_hierarchy):
        content = toml.load(self._load_file(file))
        return self.get_version(content,
            self._get_version(version_hierarchy))
