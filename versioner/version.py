# -*- coding: utf-8 -*-


class Version(object):

    def inc_patch(self, version):
        major, minor, patch = self._split(version)
        return self._join(major, minor, self._inc(patch))

    def inc_minor(self, version):
        major, minor, patch = self._split(version)
        return self._join(major, self._inc(minor), "0")

    def inc_major(self, version):
        major, minor, patch = self._split(version)
        return self._join(self._inc(major), "0", "0")

    def _join(self, major, minor, patch):
        return ".".join([major, minor, patch])

    def _split(self, version):
        try:
            major, minor, patch = version.split(".")
            return major, minor, patch
        except:
            raise Exception("Version not as per SemVer")

    def _inc(self, number):
        try:
            return str(int(number) + 1)
        except:
            raise Exception("Version not as per SemVer")
