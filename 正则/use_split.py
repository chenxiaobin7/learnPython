import re

s = 'one1two12Tthree33four444five5six698'
p = re.compile(r'\d+').split(s)
p1 = re.compile(r'\d+').split(s, 1)
print(p)
print(p1)
print(p[0])
