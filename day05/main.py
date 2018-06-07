'''
#模块导入方法
import module_name
import module1_name,module2_name
from module_name import *

from module_name import method_name as alise_name
'''
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


