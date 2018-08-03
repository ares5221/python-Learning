from  multiprocessing import Process, Pool,freeze_support
import time,os
def Foo(i):
    time.sleep(2)
    print("in process",os.getpid())
    return i + 100
def Bar(arg):
    #该回掉函数比如访问数据库结束后，往log中写日志，也可以子进程做这个操作，但是放到这里，只需要父进程连接数据库一次
    #然后每次子进程结束后，父进程回掉写日志，避免子进程多次访问数据库
    print('-->exec done:', arg,os.getpid())
if __name__ == '__main__':
    # freeze_support() #如果在windows环境上启动多进程需要加这一句
    pool = Pool(processes=3) #允许进程池同时放入5个进程
    print("主进程",os.getpid())
    for i in range(10):
        # pool.apply_async(func=Foo, args=(i,), callback=Bar) #callback=回调
        # pool.apply(func=Foo, args=(i,)) #串行
        pool.apply_async(func=Foo, args=(i,)) #并行
    print('end')
    pool.close()
    pool.join() #进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。.join()