card_list=[]
def show():
    print("*"*50)
    print("欢迎使用【名片管理】V1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.查询名片")
    print("0.退出系统")
    print("*"*50)
def new_card():
    print("-"*50)
    print("新增名片")
    name_str=input("请输入姓名:")
    phone_str=input("请输入电话:")
    qq_str=input("请输入qq:")
    email=input("请输入邮箱:")
    card_dict={"name":name_str,
               "phone":phone_str,
               "qq":qq_str,
               "email":email}
    card_list.append(card_dict)
    print(card_list)
    print("添加%s的名片成功"%name_str)
def show_all():
    print("-"*50)
    print("显示名片")
    if len(card_list)==0:
        print("无任何名片,请重新添加")
        return
    for name in ["姓名","电话","qq","邮箱"]:
        print(name,end="\t\t")
    print("")
    print("="*50)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t"%(card_dict["name"],card_dict["phone"],card_dict["qq"],card_dict["email"]))
def find_card():
        print("-"*50)
        print("查询名片")
        find_name=input("请输入要查询的姓名:")
        for card_dict in card_list:
            if card_dict["name"]==find_name:
                print("找到了")
                print("姓名\t\t电话\t\tqq\t\t邮箱")
                print("*"*50)
                print("%s\t\t%s\t\t%s\t\t%s\t\t"%(card_dict["name"],card_dict["phone"],card_dict["qq"],card_dict["email"]))
                #TODO 针对找到的名片记录执行修改和删除的操作
                deal_card(card_dict)    #实参
                break
        else:
            print("没找到%s"%find_name+",请重新输入")
def deal_card(find_dict):    #形参
    print(find_dict)

    ac_str=input("[1]修改  [2]删除  [0]返回上级 请选择要执行的操作:")
    if ac_str == "1":
        find_dict["name"]=input_card_info(find_dict["name"],"姓名:")
        find_dict["phone"]=input_card_info(find_dict["phone"],"电话:")
        find_dict["qq"]=input_card_info(find_dict["qq"],"qq:")
        find_dict["email"]=input_card_info(find_dict["email"],"邮箱:")

        print("修改名片成功！")
    elif ac_str=="2":
        card_list.remove(find_dict)

        print("删除名片成功！")

def input_card_info(dict_value,tip_message):
    re_str=input(tip_message)
    if len(re_str)>0:
        return  re_str
    else:
        return dict_value



