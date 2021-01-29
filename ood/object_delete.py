import sys


class Person(object):

    def __init__(self):
        self.name = "leo"
        print("这是构造函数")
        self.fp = open('xx.txt', 'w')

    def greet(self):
        print("hello,我的名字是%s" % self.name)

    def write(self, message):
        self.fp.write(message)

    def __del__(self):
        print("这是析构函数")
        self.fp.close()


p = Person()
p.greet()
p.write('xxx')
p2 = p
# 引用计数
# (temp = p)
print(sys.getrefcount(p))
