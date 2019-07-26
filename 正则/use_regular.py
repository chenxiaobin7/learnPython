import re

# 将正则表达式编译
pattern = re.compile(r'hello', re.I)
print(dir(pattern))

# 通过match进行匹配
rest = pattern.match('Hello,world!')
print(rest)

# 不编译直接写re.matrch(正则表达式,匹配的字符串,匹配的参数)
print(re.match(r'hello', 'Hello,world!', re.I))

# 找出以下字符串得数字
conent = 'one1two12Tthree33four444five5six698'

# 使用编译的对象
p = re.compile(r'\d+')
rest = p.findall(conent)
print(rest)
print(rest[0])
p1 = re.compile(r'[a-z]+', re.I).findall(conent)
print(p1)

# 不使用编译的对象
all = re.findall(r'[a-z]+', conent, re.I)
print(all)

#  search(pattern, string, flags=0)
conent1 = 'hello world!'
p = re.compile(r'world')
rest1 = p.search(conent1)
print(rest1)

# 使用match

rest_match = p.match(conent1)
print(rest_match)
conent2 = 'world hello!'
rest_match1 = p.match(conent2)
print(rest_match1)
# match vs search

# 区别： 查找方式不同: match只能在开头找(第一个找)，没有找到就返回None。 serach是一直找，找到最后。

# 使用函数进行调用
rest_func = re.search(r'world', conent1)
print(rest_func)

# group(num):返回整个匹配对象或编号为num的特定子组
# groups():返回一个包含所有匹配子组的元组（如果没有成功匹配，则返回一个空元组）
def test_group():
    conent3 = 'hello world!'
    res = re.compile(r'world').search(conent3)
    print(res)
    if rest:
        # group的使用
        print(res.group())
        print(res.groups())

def test_id_card():
    """身份证号码匹配"""
    p = re.compile(r'(\d{6})(?P<year>\d{4})((?P<month>\d{2})(?P<day>\d{2}))\d{2}(\d{1})([0-9]|X)')
    id1 = '430656199610015493'
    id2 = '43065619961001548X'
    rest1 = p.search(id1)
    print(rest1.group())
    print(rest1.group(1))
    print(rest1.group(4, 5))
    print(rest1.groups())
    # groupdict
    print(rest1.groupdict())


if __name__ == "__main__":
    test_group()
    test_id_card()








