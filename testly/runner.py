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
            for result in self.run_test(test):
                yield result

    def run_test(self, test):
        '''
        Runs the test in isolation and returns the result
        '''
        return test()

    def __nonzero__(self):
        return True


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
            emit('.')
        else:
            emit('E')
    emit('\n')
    if runner:
        return 0
    else:
        return str(r)
