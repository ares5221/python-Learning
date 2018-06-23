#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/6/21'
"""
class animal(object):
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("%s is eating" % self.name)
    def drink(self):
        print("%s is drinking" % self.name)
    def bobo(self):
        print("%s is pepeing" % self.name)
    def sleep(self):
        print("%s is sleeping" %self.name)

class cat(animal):
    def __init__(self,name,color):
        super(cat,self).__init__(name)
        self.color = color
    def meow(self):
        print("%s is MeowMeowMeow %s" % (self.name, self.color))

class dog(animal):
    def __init__(self,name, race):
        super(dog, self).__init__(name)
        self.race = race
    def bark(self):
        print("%s is barking race is %s" % (self.name, self.race))

cat1 = cat("Kitty","yellow")
cat1.eat()
cat1.meow()

dog11 = dog("Jessic", "teddy")
dog11.sleep()
dog11.bark()