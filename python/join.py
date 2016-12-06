from multiprocessing import Process
import os

def worker(n):
    print 'hello world', n

if __name__ == '__main__':
    print 'parent process id:', os.getppid()
    for n in range(5):
        p = Process(target=worker, args=(n,))
        p.start()
        #p.join()
        print 'child process id:', p.pid
        print 'child process name:', p.name
