from testly.finder import Finder


def test_finds_modules_in_cwd():
    finder = Finder()
    for test in finder:
        assert test.path == 'tests.test_finds_tests'
        break
    else:
        assert False, "Found too many tests"
