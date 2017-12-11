#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import fire

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
            sys.stdout.write(versioner.read(file, key_depth))
        except Exception, e:
            sys.exit(e)


def CLI():
    fire.Fire(CommandLine)


if __name__ == "__main__":
    CLI()
