def add(a,b):
    result = a+b
    print(result)

# 位置参数：严格按照函数定义时候的参数顺序传递的参数
add(1,2)

# 关键字参数：按照参数的名字来传递
add(a=1,b=2)
add(b=2,a=1)

# 混合参数：传递函数的时候既包括位置参数也包括关键字参数
# 位置参数必须要在关键字参数的前面
add(1,b=2)

# 缺省参数（不定长） args是一个元组 kwargs是一个字典，位置参数必须要在关键字参数的前面
# 这两种组合可以代表任意的参数
def add2(*args,**kwargs):
    print(args)
    print(kwargs)


add2(1,2,3,4,c=2,d=3)

# 默认参数,默认参数只能在其他参数的后面
# 如果默认参数和缺省的位置参数和关键字参数组合在一起，那么要放在缺省参数的前面
def greet(username,age=18):
    print(username)
    print(age)

greet('leo')
greet('leo',20)



