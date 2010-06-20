from testly.finder import Finder
from testly.testcase import TestModule


def test_finds_modules_in_cwd():
    finder = Finder()
    lst = [test.name for test in finder]
    assert lst == ['tests.test_finds_tests'], "Got %s" % lst

def test_finds_tests():
    module = TestModule('.', './tests', 'test_finds_tests.py')
    assert set(module) == \
        set([test_finds_modules_in_cwd, test_finds_tests])
