import os
import re
import types


test_regex = re.compile('^test_.*$')

class TestModule(object):

    def __init__(self, top, dirpath, name):
        testname = os.path.join(dirpath, name)[len(top):]
        self.path = testname
        module = os.path.splitext(testname)[0][1:].replace('/', '.')
        self.name = module
        self.module = __import__(self.name, fromlist=True)

    def __iter__(self):
        for item in dir(self.module):
            if not test_regex.match(item):
                continue
            yield getattr(self.module, item)

    def __call__(self):
        for item in self:
            result = item()
            if isinstance(result, types.GeneratorType):
                # Generator test
                for func, args in result:
                    yield func(*args)
                # Normal test
            else:
                yield True
