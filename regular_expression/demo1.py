import re

# 1.匹配某个字符串
text1 = "hello"

# match 只能从开始位置匹配,整个要用search
ret = re.match('he', text1)
print(ret.group())  # 把匹配到的字符串提取出来

# 2.点：匹配任意的字符,但是不能匹配换行符
text2 = "ahello"
ret = re.match('.', text2)
print(ret.group())

# 3. \d: 匹配任意的数字（0-9）
text3 = "123"
ret = re.match('\d', text3)
print(ret.group())

# 4. \D:匹配任意的非数字
text4 = "+a"
ret = re.match('\D', text4)
print(ret.group())

# 5. \s:匹配空白字符(\n \t \r 空格)
text5 = " +ab"
ret = re.match('\s', text5)
print(ret.group())

# 6. \w:匹配a-z,A-Z,数字以及下划线

