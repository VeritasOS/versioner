# -*- coding: utf-8 -*-

import os
import json
from collections import OrderedDict
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap
import toml

from .version import Version


class Parser(object):

    def _load_file(self, file, mode):
        """
        Check file existance and return file instance
        """
        path = os.path.abspath(file) if file else os.path.join(
            os.getcwd(), self.FILE)
        return open(path, mode)

    def _get_key_depth(self, key_depth):
        return key_depth if key_depth else self.VERSION

    def get_value(self, config, path):
        return self._get_or_update_value(config, path)

    def update_value(self, config, path, fn=None):
        return self._get_or_update_value(config, path, fn)

    def _get_or_update_value(self, config, path, fn=None):
        '''
        Function to get or update a version
        for yaml, json etc
        '''
        for var in path:
            value = config[var]
            if type(value) in [dict, OrderedDict, CommentedMap]:
                if len(path[1:]) > 0:
                    return self._get_or_update_value(value, path[1:], fn)
                else:
                    # if traverse path is empty
                    # return dict as it is
                    return value
            else:
                # If function is provided
                # update version or else get version
                if fn:
                    config[var] = fn(value)
                else:
                    return value

    def read(self, file, key_depth):
        content = self.get_content(
            self._load_file(file, 'r'))
        return self.get_value(content,
            self._get_key_depth(key_depth))

    def write(self, major, minor, patch,
              file, key_depth):

        version = Version()
        if patch:
            fn = version.inc_patch
        elif minor:
            fn = version.inc_minor
        elif major:
            fn = version.inc_major
        else:
            raise Exception("Please provide any of --inc-major, --inc-minor, --inc-patch")

        content = self.get_content(
            self._load_file(file, 'r'))
        depth = self._get_key_depth(key_depth)

        self.update_value(content, depth, fn=fn)
        return self.write_content(content,
                  self._load_file(file, 'w'))


class JSONParser(Parser):

    def get_content(self, fl):
        return json.load(fl, object_pairs_hook=OrderedDict)

    def write_content(self, content, fl):
        return json.dump(content, fl, indent=2,
                         separators=(',', ': '))


class YAMLParser(Parser):

    def get_content(self, fl):
        return YAML(typ='rt').load(fl)

    def write_content(self, content, fl):
        yaml = YAML()
        yaml.indent(mapping=2, sequence=4, offset=2)
        yaml.default_flow_style = False
        return yaml.dump(content, fl)


class TOMLParser(Parser):

    def get_content(self, fl):
        return toml.load(fl, _dict=OrderedDict)

    def write_content(self, content, fl):
        return toml.dump(content, fl)
