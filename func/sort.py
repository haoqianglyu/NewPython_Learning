# numbers = [20,11,9,30]
# numbers.sort(reverse=True)
# print(numbers)
from functools import cmp_to_key
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
        'age':18
    }
]

def cmp(a,b):
    # 如果返回的是一个大于0的值，那么代表a>b
    # 如果返回的是一个小于0的值，那么代表a<b
    # 如果返回的是一个等于0的值，那么代表a=b
    if a['age']>b['age']:
        return 1
    elif a['age']<b['age']:
        return -1
    else:
        if a['name'] > b['name']:
            return 1
        else:
            return -1

persons.sort(key=cmp_to_key(cmp))
print(persons)

# sorted不更改原来的顺序，而是返回一个排序后的新的列表，sort会改变原来的顺序
new_persons = sorted(persons,key=cmp_to_key(cmp))