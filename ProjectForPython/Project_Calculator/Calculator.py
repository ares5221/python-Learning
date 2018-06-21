#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/6/20'
"""
import re
import functools
def calc(formula):
    '''计算程序主入口, 主要逻辑是先计算括号里的值,算出来后再算乘除,再算加减'''
    parenthesise_flag = True
    calc_res = None  #初始化运算结果为None
    while parenthesise_flag:
        #re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
        m = re.search("\([^()]*\)", formula)  #找到最里层的括号 先转义字符\( \),[^()]匹配除了()之外的字符，*重复匹配0或多个表达式
        if m:
            #group([group1,...]) 获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。
            # group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；不填写参数时，返回group(0)；
            # 没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
            print("先算括号里的值:",m.group())
            sub_res = compute(m.group())
            formula = formula.replace(m.group(), str(sub_res))
        else:
            #print('\033[41;1m----没括号了...---\033[0m')
            print('\n\n\033[40;1m最终结果:\033[0m', compute(formula))
            parenthesise_flag = False  # 代表公式里的拓号已经都被剥除啦

def remove_duplicates(formula):
    formula = formula.replace("++","+")
    formula = formula.replace("+-","-")
    formula = formula.replace("-+","-")
    formula = formula.replace("--","+")
    formula = formula.replace("- -","+")
    return formula

def compute_mutiply_and_dividend(formula):
    '''算乘除,传进来的是字符串'''
    operators = re.findall("[*/]", formula)
    calc_list = re.split("[*/]", formula)
    res = None
    for index, i in enumerate(calc_list):
        if res:
            if operators[index - 1] == "*":
                res *= float(i)
            elif operators[index - 1] == "/":
                res /= float(i)
        else:
            res = float(i)
    print("\033[31;1m[%s]运算结果=\033[0m" % formula, res)
    return res

def handle_minus_in_list(operator_list, calc_list):
    '''有的时候把算术符和值分开后,会出现这种情况  ['-', '-', '-'] [' ', '14969037.996825399 ', ' ', '12.0/ 10.0 ']
       这需要把第2个列表中的空格都变成负号并与其后面的值拼起来,恶心死了
    '''
    for index, i in enumerate(calc_list):
        if i == '':  # 它其实是代表负号,改成负号
            calc_list[index + 1] = i + calc_list[index + 1].strip()

def handle_special_occactions(plus_and_minus_operators, multiply_and_dividend):
    '''有时会出现这种情况 , ['-', '-'] ['1 ', ' 2 * ', '14969036.7968254'],2*...后面这段实际是 2*-14969036.7968254,需要特别处理下,太恶心了'''
    for index, i in enumerate(multiply_and_dividend):
        i = i.strip()
        if i.endswith("*") or i.endswith("/"):
            multiply_and_dividend[index] = multiply_and_dividend[index] + plus_and_minus_operators[index] + \
                                           multiply_and_dividend[index + 1]
            del multiply_and_dividend[index + 1]
            del plus_and_minus_operators[index]
    return plus_and_minus_operators, multiply_and_dividend

def minus_operator_handler(formula):
    '''处理一些特殊的减号运算'''
    minus_operators = re.split("-",formula)
    calc_list= re.findall("[0-9]",formula)
    if minus_operators[0] == '': #第一值肯定是负号
        calc_list[0] = '-%s' % calc_list[0]
    res = functools.reduce(lambda x,y:float(x) - float(y), calc_list)
    print("\033[33;1m减号[%s]处理结果:\033[0m" % formula, res )
    return res

def compute(formula):
    '''这里计算的是不带括号的公式'''
    formula = formula.strip("()")  # 去除外面包的拓号
    formula = remove_duplicates(formula)  # 去除外重复的+-号
    plus_and_minus_operators = re.findall("[+-]", formula)
    multiply_and_dividend = re.split("[+-]", formula)  # 取出乘除公式
    if len(multiply_and_dividend[0].strip()) == 0:  # 代表这肯定是个减号
        multiply_and_dividend[1] = plus_and_minus_operators[0] + multiply_and_dividend[1]
        del multiply_and_dividend[0]
        del plus_and_minus_operators[0]
    plus_and_minus_operators, multiply_and_dividend = handle_special_occactions(plus_and_minus_operators,multiply_and_dividend)
    for index, i in enumerate(multiply_and_dividend):
        if re.search("[*/]", i):
            sub_res = compute_mutiply_and_dividend(i)
            multiply_and_dividend[index] = sub_res
    # 开始运算+,-
    print(multiply_and_dividend, plus_and_minus_operators)
    total_res = None
    for index, item in enumerate(multiply_and_dividend):
        if total_res:  # 代表不是第一次循环
            if plus_and_minus_operators[index - 1] == '+':
                total_res += float(item)
            elif plus_and_minus_operators[index - 1] == '-':
                total_res -= float(item)
        else:
            total_res = float(item)
    print("\033[32;1m[%s]运算结果:\033[0m" % formula, total_res)
    return total_res
if __name__ == '__main__':
    # res = calc("1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )")
    res = calc("1 - 2 * ( (60-30 +(-9-2-5-2*3-5/3-40*4/2-3/5+6*3) * (-9-2-5-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )")

