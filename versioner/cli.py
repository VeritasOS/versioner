#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import fire

from .versioner import (
    Versioner
)


class CommandLine(object):

    def read(self, package_manager, file="", version_hierarchy=[]):
        versioner = Versioner(package_manager)
        try:
            # TODO: Some how version_hierarchy is string
            # when only item in version_hierarchy
            # something to do with fire
            if type(version_hierarchy) == str:
                version_hierarchy = [version_hierarchy]
            print versioner.read(file, version_hierarchy)
        except Exception, e:
            sys.exit(e)


def CLI():
    fire.Fire(CommandLine)


if __name__ == "__main__":
    CLI()
