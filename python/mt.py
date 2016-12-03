#!/usr/bin/python

import threading
import thread
import time

threadLock = threading.Lock()

def print_time(threadName,delay):
	threadLock.acquire()
	count = 0
	while count < 5:
		time.sleep(delay)
		count+=1
		print "%s: %s" % (threadName, time.ctime(time.time()))
	threadLock.release()

try:
	thread.start_new_thread(print_time, ("Thread-1",2,))
	thread.start_new_thread(print_time, ("Thread-2",4,))
except:
	print "Error"

while 1:
	pass
