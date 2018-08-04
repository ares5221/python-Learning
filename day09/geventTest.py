#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gevent
def foo():
    print('Running in foo') #1
    gevent.sleep(2) #2
    print('Explicit context switch to foo again') #3

def bar():
    print('Explicit context to bar') #4
    gevent.sleep(1) #5
    print('Implicit context switch back to bar') #6

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])