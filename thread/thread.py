# encoding: utf-8
__author__ = 'wudi'

import thread
import threading
import time_test

class Clock(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        while 1:
            print "%d Id : %d" % (time_test.time_test(), self.id)
            pass


if __name__ == '__main__':
    c1 = Clock(1)
    c2 = Clock(2)

    c1.start()
    c2.start()