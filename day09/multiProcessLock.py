from multiprocessing import Process, Lock
'''进程锁'''
def f(l,i):
    l.acquire()
    print('Hello World',i)
    l.release()

if __name__ == '__main__':
    lock = Lock()
    for num in range(10):
        Process(target=f, args=(lock,num)).start()