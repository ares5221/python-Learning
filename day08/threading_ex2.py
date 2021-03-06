import threading
import time

class MyThread(threading.Thread):
    def __init__(self,n,sleep_time):
        super(MyThread,self).__init__()
        self.n =  n
        self.sleep_time = sleep_time
    def run(self):
        print("runnint task ",self.n )
        time.sleep(self.sleep_time)
        print("task done,",self.n )

t1 = MyThread("t1",2)
t2 = MyThread("t2",4)

t1.start()
t2.start()
# t1启动后等待2s，t2等待4s 都结束后主线程结束输出main thread
t1.join() #=wait()等待t1执行结束
t2.join()

print("main thread....")
