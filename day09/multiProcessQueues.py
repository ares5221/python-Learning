from multiprocessing import Process, Queue
def f(qq):
    print('in child:',)
    qq.put([42, None, 'child process put '])
#父进程起了进程队列q，在生成子进程p时候把这个q传给他，在父进程可以访问到子进程数据
# 看起来好像两个进程共享了一个Queue，实际上克隆了一个Queue
# 通过中间方序列化再反序列化pickle实现
if __name__ == '__main__':
    # q = queue.Queue()
    # p = threading.Thread(target=f,)
    q = Queue()
    q.put("main process put ")
    p = Process(target=f, args=(q,))
    p.start()
    # print(q.get())  # prints "[42, None, 'hello']"
    p.join()
    print("333", q.get_nowait())
    print("333", q.get_nowait())
