'''
Created on Jun 25, 2015

@author: jyhu
'''

import threading
import time
import random

global_count = 0
global_lock = threading.Lock()

class ThreadLock(threading.Thread):
    '''
    classdocs
    '''

    def run(self):
        global global_count
        global global_lock
        time.sleep(random.random())
        if global_lock.acquire():
            global_count += 1
            
            time.sleep(random.random())
            print "after %s : count is %d"%(self.name, global_count)
            global_lock.release()
        

if __name__ == '__main__':
    for i in range(10):
        ThreadLock().start()