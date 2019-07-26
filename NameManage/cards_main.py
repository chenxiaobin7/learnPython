#! /usr/bin/python3

#在cards_main.py 的目录NameManage下添加 chmod +x cards_main.py修改此文件的权限
#即是不需要python3 cards_main.py这个命令，也是不需要python3的解释器
#前提是要在cards_main.py这个python file里面添加  #! /user/bin/python3
#/user/bin/python3 同样在NameManage下输入which python3
import cards_tools
while True:
    cards_tools.show()
    str=input("希望执行的操作:")
    print("你选择的操作是[%s]"%str)
    if str in ["1","2","3"]:
        if str =="1":
            cards_tools.new_card()
        elif str =="2":
            cards_tools.show_all()
        elif str =="3":
            cards_tools.find_card()
        pass
    elif str=="0":
        print("欢迎再次使用本系统")
        break
    else:
        print("输入不准确,重新输入")