import multiprocessing
import time
# python3的range就是xrange。通过在不同环境下type(range(10)) 可以查看发现
# python2中，range的返回值是list，这意味着内存将会分布相应的长度的空间给list。
# python3中返回的是一个对象，并没有将数据完全实例化，所以内存中只有一个对象的空间，对性能优化还是很有帮助的。
# 类似的改动是有很多的，例如：字典的items.
def proc1(pipe):
    while True:
        for i in range(10000):
            print("send: %s" % (i))
            pipe.send(i)
            time.sleep(1)

def proc2(pipe):
    while True:
        print("proc2 rev:", pipe.recv())
        time.sleep(1)

def proc3(pipe):
    while True:
        print("PROC3 rev:", pipe.recv())
        time.sleep(1)

if __name__ == "__main__":
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc1, args=(pipe[0],))
    p2 = multiprocessing.Process(target=proc2, args=(pipe[1],))
    # p3 = multiprocessing.Process(target=proc3, args=(pipe[1],))

    p1.start()
    p2.start()
    # p3.start()

    p1.join()
    p2.join()
    # p3.join()
# pipe()返回两个连接对象代表pipe的两端。每个连接对象都有send()方法和recv()方法。
# 但是如果两个进程或线程对象同时读取或写入管道两端的数据时，管道中的数据有可能会损坏。
# 当进程使用的是管道两端的不同的数据则不会有数据损坏的风险。