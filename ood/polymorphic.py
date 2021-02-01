# class Person(object):
#     def eat(self):
#         pass
#
#
# class Student(Person):
#     def eat(self):
#         pass
#
#
# class Teacher(Person):
#     def eat(self):
#         pass
#
# def greet(Person p):
#     p.eat()

# 鸭子类型：


class Hero(object):
    def __init__(self):
        pass

    def stroke(self):
        pass


class Chenyaojin(Hero):
    def stroke(self):
        print("陈咬金的回血大招")


class Xiangyu(Hero):
    def stroke(self):
        print("项羽的推人大招")


hero = None
value = input("请输入英雄：")
if value == "1":
    hero = Chenyaojin()
else:
    hero = Xiangyu()

hero.stroke()
