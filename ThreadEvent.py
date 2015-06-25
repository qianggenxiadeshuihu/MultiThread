'''
Created on Jun 25, 2015

@author: jyhu
'''

import threading
import time
import random

global_count = 0

class AnotherThread(threading.Thread):
    def __init__(self, threadName, a_signal):
        threading.Thread.__init__(self, name = threadName)
        self.a_signal = a_signal
        
    def run(self):
        while True:
            raw_input()
            print self.name
            self.a_signal.set()
        
class ThreadEvent(threading.Thread):
    '''
    classdocs
    '''

    def __init__(self, threadName):
        threading.Thread.__init__(self, name = threadName)
        
        
    def run(self):
        global global_count
        
        a_sig = threading.Event()
        self.threadEvent = a_sig
        AnotherThread("branch process", a_sig).start()
        
        while True:
            global_count += 1
            if not (global_count % 10):
                self.threadEvent.wait()
                self.threadEvent.clear()
                
            print self.name + str(global_count)
        

if __name__ == '__main__':
    
    ThreadEvent("master process").start()