# 类属性

class Person(object):
    country = 'china'

    def __init__(self, name,country):
        self.name = name
        self.country = country

    def greet(self):
        # 如果对象上没有country属性，那么通过self和Person.country得到的效果是一样的
        # 都是访问Person的类属性
        # 如果给对象绑定了country属性，那么通过self.country访问到的就是这个对象上的属性
        # 通过Person.country访问到的就是类属性
        print("hello my name is %s,i am from %s" % (self.name, Person.country, self.country))


# 实例属性:
# 绑定到对象上的属性就是实例属性
# 实例属性只在当前对象上有作用
p1 = Person("leo")
p1.age = 18
print(p1.name)

p2 = Person('william')
# print(p2.age)
print(p2.name)

# 类属性:
# 如何在类中定义类属性：
# 类属性可以通过对象进行访问
# 如果通过对象修改类属性，那么其实不是修改类属性，
# 而是在这个对象上面重新定义了一个名字相同的实例属性而已
print(p1.country)
p1.country = 'usa'
print(p1.country)
print(Person.country)

p2.country = "uk"
print(p2.country)
print(Person.country)

# 要正确修改类属性，只能通过类名的方式修改
Person.country = 'abc'
print(Person.country)

p1.greet()
