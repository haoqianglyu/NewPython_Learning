# 多继承
class Ma(object):
    def run(self):
        print("马在奔跑")

    def eat(self):
        print("马在吃草")


class Lv(object):
    def lamo(self):
        print("驴在拉磨")

    def eat(self):
        print("驴在吃麦秆")


class Luozi(Ma, Lv):
    pass

    def eat(self):
        # 如果不想按照mro的顺序执行，可以通过以下方式执行
        Lv.eat(self)
        print("骡子在吃稻谷")


lz = Luozi()

print(Luozi.mro())
lz.run()
lz.lamo()
lz.eat()
