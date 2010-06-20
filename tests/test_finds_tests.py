from testly.finder import Finder


def test_finds_modules_in_cwd():
    finder = Finder()
    lst = [test.name for test in finder]
    assert lst == ['tests.test_finds_tests'], "Got %s" % lst
