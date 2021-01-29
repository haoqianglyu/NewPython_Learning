# 受保护属性或者方法

class Women(object):

    def __init__(self, age):
        # 定义一个受保护的age属性
        self._age = age


woman = Women(19)
print(woman._age)


# 私有的属性或者方法
class Account(object):

    def __init__(self, a_id, password):
        self.a_id = a_id
        # 定义一个私有的age属性
        self.__password = password

    # 私有方法
    def __account_list(self):
        print("我是一个私有方法")
        return [11, -11, 22]

    def get_account_list(self, password):
        if password == self.__password:
            return self.__account_list()
        else:
            return None


account1 = Account('xxxxx', '123456')
# print(account1.__password)
# account1.__account_list()
account1.get_account_list('123456')

# 实在想拿到：
print(account1._Account__password)

# __init__ 不是私有方法
