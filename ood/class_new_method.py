class Person(object):

    # new方法先执行
    def __new__(cls, *args, **kwargs):
        print("Person的new方法调用")
        print("=" * 10)
        print(args)
        print(kwargs)
        # 1.new方法执行完后一定要记得返回父类的调用
        # 2.如果父类是object,调用__new__方法的手不能接受除cls之外的参数
        return super().__new__(cls)

    def __init__(self, name):
        print("name:%s" % name)
        self.name = name


class Student(Person):
    def __new__(cls, *args, **kwargs):
        print("student的new方法")
        # 如果父类不是object，那么可以选择传递
        return super().__new__(cls, name=args[0])

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("leo")

Student("xxx", 18)
