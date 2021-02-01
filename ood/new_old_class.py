# 旧式类 ：没有指定任何父类
# 在Python2.2版本之前，所有的类都是旧式类
class Person():
    def __init__(self, name):
        self.name = name


# 在旧式类中，子类不能使用super函数来调用父类的函数

# 子类也是旧式类
class Student(Person):
    def __init__(self, name):
        print("这是student类")
        # super(Student, self).__init__(name)
        # 旧式类中如果想要调用父类的方法，必须通过以下的形式：
        # 父类名.方法名(self,其他参数)
        Person.__init__(self, name)


# 新式类：直接或者间接继承自obj类
# class Person(object):
#     def __init__(self, name):
#         self.name = name

s1 = Student('leo')
print(s1.name)

print(type(s1))
print(s1.__class__)
