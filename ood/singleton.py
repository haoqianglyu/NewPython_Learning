# 单例设计模式，某个类整个程序运行期间最多只能有一个对象被创建


class User(object):
    # 私有属性
    __instance = None

    def __new__(cls, *args, **kwargs):
        # if not cls.__instance:
        #     return super().__new__(cls)
        # else:
        #     return  cls.__instance
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    # def __init__(self,name):
    #     pass


user1 = User("william")
user2 = User("leo")
print(id(user1))
print(id(user2))
