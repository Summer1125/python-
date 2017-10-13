
products_list = [["iphone6",2000],
            ["iphone7",3000],
            ["iphone8",5000],
            ["iphoneX",8000]]
import sys
import os
import getpass
count = 0
flag = True
bag = {}
users = "user_file.txt"
product = "products.txt"
bag_data = "shopping_bag.txt"

with open(bag_data) as fp_bag:
    data_tmp = fp_bag.read().strip()
    bag = eval(data_tmp)
#print(bag)

while flag:
    user_name = input(">>UserName:").strip()
    with open(users) as fp
        if user_name == user_tmp:
                password = getpass.getpass(">>PassWord:").strip()
                if password == passwd_tmp:
                    print(">>欢迎登录，你的余额：%s元<<"%balance)
                    with open(bag_data) as fp3:
                        data_tmp = eval(fp3.read().strip())
                        data_user = data_tmp[user_name]
                        print("购物历史\n"+str(data_user))

                    flag = False
                else:
                    print("用户名或密码错误，请重新输入。")
while True:
    id = 1
    print("你可买以下商品：")
    for i in products_list:
        print(id,i[0],i[1])
        id += 1
    choise = input(">>输入产品编号,或者'q'退出：").strip()
    if choise.isdigit():
        choise = int(choise)
        if choise >=1 and choise < id:
            p_name = products_list[choise-1][0]
            p_price = products_list[choise-1][1]
            if balance < p_price:
                diff = p_price - balance
                yn = input(">>余额不足，是否进行充值(y/n)？:").strip()
                if yn == "y":
                    top_up = int(input(">>充值金额：").strip())
                    balance  += top_up
                elif yn == 'n':
                    choise = "q"
                else:
                    print("输入错误！")

            else:
                prodct_key = bag[user_name].keys()
                if p_name in prodct_key:
                    bag[user_name][p_name][1] += 1
                else:
                    bag[user_name][p_name] = [p_price,1]
                balance -= p_price
                print("%s已经加入购物车"%p_name)
                print("已经购买的商品：",bag[user_name],"余额%s"%balance)
        else:
            print("请输入正确的商品编号或退出！")
    elif choise == 'q':
        id_count = 1
        print(bag)
        with open("shopping_bag.txt","w") as fp2:
             fp2.write(str(bag))
        print("************Your shopping list*********")
        print("id    products    quantity    price    total")
        for key in bag[user_name].keys():
            msg = "%s     %s       %s         %s     %s"%(id_count,
                                                          key,
                                                          bag[user_name][key][1],
                                                          bag[user_name][key][0],
                                                          bag[user_name][key][0]*bag[user_name][key][1])
            print(msg)
            id_count += 1
        print("Your current Balance:",balance)
        print("*****************end*******************")
        break


    else:
        print("请输入正确的产品编号！")