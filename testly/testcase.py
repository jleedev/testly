import os


class TestCase(object):

    def __init__(self, top, dirpath, name):
        testname = os.path.join(dirpath, name)[len(top):]
        self.path = testname
        module = os.path.splitext(testname)[0][1:].replace('/', '.')
        self.name = module

    def __call__(self):
        self.module = __import__(self.name)
