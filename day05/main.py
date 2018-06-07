'''
模块用来从逻辑上组织python代码
包用来从逻辑上组织模块，本质是一个目录
#模块导入方法
import module_name
import module1_name,module2_name
from module_name import *

from module_name import method_name as alise_name
'''
#import本质
#导入模块的本质就是把python文件解释一遍
#导入包的本事就是执行该包下的__init__.py文件
import sys,os
print(sys.path)

x=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(x)

from t import *
#print(t.name)
#t.say_hello()
logger()
def logger():
    print ('in the main')
logger()


