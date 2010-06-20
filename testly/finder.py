from os import getcwd, walk
import os.path
import re

from testly.testcase import TestModule


module_regex = re.compile('^test_.*.py$')


class Finder(object):

    def __init__(self, cwd=None):
        if cwd is None:
            self.top = getcwd()
        else:
            self.top = cwd

    def __iter__(self):
        for dirpath, dirnames, filenames in walk(self.top):
            if os.path.split(dirpath)[1] == 'tests':
                for name in filenames:
                    if module_regex.match(name):
                        yield TestModule(self.top, dirpath, name)
