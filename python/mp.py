from multiprocessing import Process

import os

def worker(name):
	print name
	print 'parent process id:', os.getppid()
	print 'process id:',os.getpid()

if __name__ == '__main__':
	p = Process(target=worker,args=('function worker.',))
	p.start()
	p.join()
	print p.name
