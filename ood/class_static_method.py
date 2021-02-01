class Person(object):

    country = 'china'

    def eat(self):
        print("hello world")

    # 装饰器
    @classmethod  # 变成类方法
    def greet(cls):  # 必须是当前这个类，通过cls获取
        cls.country = 'usa'
        print("leo")

    # 静态方法,不需要传递对象或者类
    # 使用场景：不需要修改类或者对象的属性的时候，并且这个方法放在这个类中可以让代码更加有管理性
    @staticmethod
    def static_method():
        print("hello")
        Person.country = "ccc"


# 实例方法
p1 = Person()
p1.eat()

# 类方法
# 调用方式：使用类名  使用对象
print(Person.country)
Person.greet()
p1.greet()
print(Person.country)

# 静态方法
# 调用方式：使用类名  使用对象
Person.static_method()
p1.static_method()
print(Person.country)

