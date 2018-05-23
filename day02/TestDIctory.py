dic = {
    'stu1001': "lvxiaoshu",
    'stu1002': "lvxiaoyu",
    'stu1003': "chenzuan",
    'stu1004': "caoqingci",
    'stu1005': "chengqiuqiao",
}
#check
print(dic.get("stu1003"))
#print(dic["stu1004"])
#update
dic["stu1004"] = "曹青辞"
#add
dic["stu1006"] = "新亭侯"
#del
del dic["stu1001"]
dic.pop("stu1002")
#dic.popitem()
#判断字典中是否存在某元素，有则返回true
print("stu1003" in dic)
print(dic)

dic["stu1004"] = "曹青辞"
'''
#update 两个字典有共同的key则更新其value，没有则合并
info = {'stu1102': 'LongZe Luola', 'stu1103': 'XiaoZe Maliya', 'stu1106': 'Alex'}
b = {1:2,3:4, "stu1102":"龙泽萝拉"}
info.update(b)
print(info)  #{'stu1102': '龙泽萝拉', 1: 2, 3: 4, 'stu1103': 'XiaoZe Maliya', 'stu1106': 'Alex'}

#items
info.items()
#dict_items([('stu1102', '龙泽萝拉'), (1, 2), (3, 4), ('stu1103', 'XiaoZe Maliya'), ('stu1106', 'Alex')])

#通过一个列表生成默认dict,有个没办法解释的坑，少用吧这个
#dict.fromkeys([1,2,3],'testd')
#{1: 'testd', 2: 'testd', 3: 'testd'}
'''
#循环dic方法1
for key in dic:
    print(key,dic[key])
'''
#方法2
for k,v in dic.items(): #会先把dict转成list,数据里大时莫用
    print(k,v)
'''