persons = [
    {
        'name':'zhangsan',
        'age':20
    },
    {
        'name':'lisi',
        'age':18
    },
    {
        'name':'wangwu',
        'age':19
    }
]
# 匿名函数：
# 定义方式： lambda x:x['age'],一般适合代码只有一行的函数

# def my_cmp(x):
#     return x['age']

persons.sort(key=lambda x:x['age'])
print(persons)

# 需求：求两个数的加减乘除，在运算之前，先对两个值乘以10
a = 10
b = 20

def calculate(a,b,func):
    a*=10
    b*=10
    result = func(a,b)
    return result

result1 = calculate(a,b,lambda x,y:x+y)
result2 = calculate(a,b,lambda x,y:x-y)
result3 = calculate(a,b,lambda x,y:x*y)
result4 = calculate(a,b,lambda x,y:x/y)

print(result1,result2,result3,result4)

a = [1,2,3,4,5,6,7,8,9]
# result = filter(lambda x:True if x>3 else False,a)
result = filter(lambda x:x>3,a)
for x in result:
    print(x)

new_result = map(lambda x:x*10,a)
for x in new_result:
    print(x)

print(list(new_result))

