from multiprocessing import Process

def worker1(n):
    print 'hello world', n
def worker2():
    print 'worker2...'

if __name__ == '__main__':
    for n in range(3):
        p1 = Process(name='worker1', target=worker1, args=(n,))
        p1.daemon = True
        p1.start()
        p1.join()
    p2 = Process(target=worker2)
    p2.daemon = False
    p2.start()
    p2.join()
