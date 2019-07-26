import re
"""使用正则j进行替换"""
s = 'one1two12Tthree33four444five5six698'
# one@two@Tthree@four@five@six@

p = re.compile(r'\d+').sub('@', s)
print(p)


p1 = s.replace('1', '@').replace('12', '@').replace('33', '@')
print(p1)

# 使用正则表达式更换位置
s2 = 'hello world'
p2 = re.compile(r'(\w+) (\w+)').sub(r'\2 \1', s2)
print(p2)

# 在原有的内容基础上替换并改变内容

def f(m):
    """使用函数进行替换规则改变"""
    return m.group(2).upper()+' '+m.group(1)
res = re.compile(r'(\w+) (\w+)').sub(f, s2)
print(res)

# 使用匿名函数进行替换 lambda
rest_lamb = re.compile(r'(\w+) (\w+)').sub(lambda m: m.group(2).upper()+' '+m.group(1), s2)
print("=====================")
print(rest_lamb)




