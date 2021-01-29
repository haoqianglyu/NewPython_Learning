# global关键字：如果想在函数或者某个代码块中修改全局变量，那么应该使用global关键字
username = "leo"
def greet():
    global username
    username = "william"
    print("hello %s" % username)

greet()
print(username)

# 针对可变数据类型，如果在函数中确实想要改变全局变量persons的指向，那么就要使用global关键字
# 如果在函数中只是想要对全局变量中的元素进行增删改查，可以不需要使用global关键字
persons = ["zhangsan","lisi"]
def add_person(name):
    # persons.append(name)
    global persons
    persons = []
    print(persons)
add_person("wangwu")
print(persons)