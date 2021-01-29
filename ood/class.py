# 1.定义类必须使用class关键字，然后继承自object类
# 2.在类中定义方法：第一个参数必须是self，self代表的是当前这个对象

class Person(object):
    def __init__(self, name1, age):
        self.name = name1
        self.age = age
        print(id(self))

    def eat(self):
        print("人这个对象在吃饭")


# 3.使用类创建一个对象： 类名()
p1 = Person('leo', 18)
p2 = Person('willam', 20)
print(p1.name)

print(id(p1))
print(id(p2))
