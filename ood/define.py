person1 = {
    'name':'leo',
    'age':18,
    'style':'wenjing'
}

person1 = {
    'name':'william',
    'age':20,
    'style':'haofang'
}
def eat(person):
    if person['style']=='wenjing':
        print("我是%s,我吃饭文静"%person['name'])
    else:
        print("我是%s,我吃饭豪放"%person['name'])

eat(person1)






person1 = {
    'name':'leo',
    'age':18,
    'style':'wenjing'
}

def eat(person):
    print("我是%s,我吃饭文静" % person['name'])

car = {
    'brand':'BMW',
    'xinghao':'5'
}

def run(car):
    print('我是%s车，型号是%s，我现在跑起来'%(car['brand'],car['xinghao']))
run(car)

print("--------------------")

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print("我是%s,我吃饭文静" % self.name)

class Car(object):
    def __init__(self,brand,xinghao):
        self.brand = brand
        self.xinghao = xinghao
    def run(self):
        print('我是%s车，型号是%s，我现在跑起来' % (self.brand, self.xinghao))

p1 = Person('leo','18')
p1.eat()

c1 = Car('BMW','5')
c1.run()