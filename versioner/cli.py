#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import fire
import json

from .versioner import (
    Versioner
)


class CommandLine(object):

    def read(self, package_manager, file="", key_depth=[]):
        versioner = Versioner(package_manager)
        try:
            # TODO: Some how key_depth is string
            # when only item in key_depth
            # something to do with fire
            if type(key_depth) == str:
                key_depth = [key_depth]
            sys.stdout.write(json.dumps(versioner.read(file, key_depth)))
        except Exception, e:
            sys.exit(e)

    def write(self, package_manager, inc_major=False, inc_minor=False,
              inc_patch=False, file="", key_depth=[]):
        versioner = Versioner(package_manager)
        try:
            if not any([inc_major, inc_minor, inc_patch]):
                raise Exception("Please provide any of --inc-major, --inc-minor, --inc-patch")

            # TODO: Some how key_depth is string
            # when only item in key_depth
            # something to do with fire
            if type(key_depth) == str:
                key_depth = [key_depth]

            versioner.write(inc_major, inc_minor,
                inc_patch, file, key_depth)
            sys.stdout.write("Version updated successfully")
        except Exception, e:
            sys.exit(e)


def CLI():
    fire.Fire(CommandLine)


if __name__ == "__main__":
    CLI()
