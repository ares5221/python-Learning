#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/6/20'
"""
class Person(object):
    def __init__(self, name, age,gender,fight):
        self.name = name
        self.age = age
        self.gender = gender
        self.fight = fight

    def FightInGrassLand(self):
        self.fight = self.fight -200
        print("%s，草丛战斗，消耗200战斗力" % self.name)
    def Xiulian(self):
        self.fight = self.fight + 100
        print("%s，自我修炼，增长100战斗力" % self.name)
    def MultiPersonGame(self):
        self.fight = self.fight - 500
        print("%s，多人游戏，消耗500战斗力" % self.name)

    def detail(self):
        print("姓名:%s ; 性别:%s ; 年龄:%s ; 战斗力:%s" % (self.name, self.gender, self.age, self.fight))

cang = Person('苍井井', '女', 18, 1000)    # 创建苍井井角色
dong = Person('东尼木木', '男', 20, 1800)  # 创建东尼木木角色
bo = Person('波多多', '女', 19, 2500)      # 创建波多多角色

cang.MultiPersonGame() #苍井空参加一次多人游戏
dong.Xiulian()#东尼木木自我修炼了一次
bo.FightInGrassLand() #波多多参加一次草丛战斗
#输出当前所有人的详细情况
cang.detail()
dong.detail()
bo.detail()

cang.MultiPersonGame() #苍井空又参加一次多人游戏
dong.MultiPersonGame() #东尼木木也参加了一个多人游戏
bo.Xiulian() #波多多自我修炼了一次
#输出当前所有人的详细情况
cang.detail()
dong.detail()
bo.detail()