def add(a,b):
    result = a+b
    return result
    print('end')
# 只会执行到return语句

value = add(1,2)
print(value)

# 可以用元组返回多个值
def greet(username,age):
    # result = {"username":username,"age":age}
    # result = [username,age]

    # print(type(result))
    return username,age
value = greet('leo',20)
username,age = greet('leo',20)
print(value)
print(type(value))

