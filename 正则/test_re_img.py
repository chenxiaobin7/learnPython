# https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2512412073,484693686&amp;fm=26&amp;gp=0.jpg
# https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2512412073,484693686&fm=26&gp=0.jpg
# https://f11.baidu.com/it/u=2465775762,1509670197&amp;fm=72
# https://f11.baidu.com/it/u=2465775762,1509670197&fm=72


# 1. 下载 html
# 2. 正则规则
# 3. 要找到img标签
# 4. 找到src属性
# <img class= "" style="" src="" xx="">
# <img.+src=\".+\".+>
import re


def test_re_img():
    """使用正则找到图片地址"""
    # 1.读取html
    with open('img.html', encoding='utf-8') as f:
        html = f.read()
    # print(html)
    # 2.准备正则
    # p1 = re.compile(r'<img.+?src=\".+?\".+?>').findall(html)
    # print(p1)
    # for ls1 in p1:
    #     print(ls1)
    p = re.compile(r'<img.+?src=\"(?P<src>.+?)\".+?>', re.M | re.I)
    # 使用findall找到图片的列表
    list_img = p.findall(html)
    print(len(list_img))
    for ls in list_img:
        print(ls.replace('&amp;', '&'))


if __name__ == "__main__":
    test_re_img()


