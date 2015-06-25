'''
Created on Jun 25, 2015

@author: jyhu
'''

import threading
import time
import random

global_flag = 0

class AnotherThread(threading.Thread):
    def __init__(self, threadName, a_signal):
        threading.Thread.__init__(self, name = threadName)
        self.threadEvent = a_signal
        
    def run(self):
        global global_flag
        while True:
            self.threadEvent.wait()
            self.threadEvent.clear()
            global_flag = 1
            
        
class ThreadMaster(threading.Thread):
    '''
    classdocs
    '''

    def __init__(self, threadName):
        threading.Thread.__init__(self, name = threadName)
        
        
    def run(self):
        global global_flag
        count = 0
        
        while True:
            time.sleep(1)
            count += 1
            if global_flag != 0:
                print self.name + "+++++++" + str(count)
                global_flag = 0
            print self.name + "--" + str(count)
        

if __name__ == '__main__':
    
    ThreadMaster("master process").start()
    a_sig = threading.Event()
    AnotherThread("branch process", a_sig).start()
    while True:
        raw_input()
        a_sig.set()
        