#!/usr/bin/python
from multiprocessing import Pool, current_process
import os, time, sys

def worker(n):
    print 'hello world', n
    print 'process name:', current_process().name 
    time.sleep(1) 

if __name__ == '__main__':
    p = Pool(processes=3)
    for i in range(8):
        r = p.apply_async(worker, args=(i,))
        r.get(timeout=5) 
    p.close()
