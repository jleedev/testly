import sys

from testly.finder import Finder


class Runner():

    def __init__(self):
        self.finder = Finder()

    def run(self):
        '''
        Runs all the tests and returns the result
        '''
        for test in self.finder:
            yield self.run_test(test)

    def run_test(self, test):
        '''
        Runs the test in isolation and returns the result
        '''
        test()

    def __nonzero__(self):
        return 1


def emit(result):
    sys.stdout.write(result)
    sys.stdout.flush()

def runner():
    '''
    Main entry point for testly, so it returns 0 on success
    and an error string on failure
    '''
    runner = Runner()
    for result in runner.run():
        if result:
            emit('E')
        else:
            emit('.')
    emit('\n')
    if runner:
        return 0
    else:
        return str(r)
