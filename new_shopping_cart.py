# 购物车
# 1. 商品信息- 数量、单价、名称
# 2. 用户信息- 帐号、密码、余额
# 3. 用户可充值
# 4. 购物历史信息
# 5. 允许用户多次购买，每次可购买多件
# 6. 余额不足时进行提醒
# 7. 用户退出时 ，输出档次购物信息
# 8. 用户下次登陆时可查看购物历史
# 9. 商品列表分级
products_list = [["iphone6",2000],
			["iphone7",3000],
			["iphone8",5000],
			["iphoneX",8000]]
import sys
import os
import getpass
count = 0
flag = True
bag = {}#购物车字典
users = "user_file.txt"
product = "products.txt"
id = 1
while flag:
    user_name = input(">>UserName:").strip()
    with open(users) as fp:
        for line in fp:
            user_tmp,passwd_tmp,balance= line.split()
            print(user_tmp,passwd_tmp)
            if user_name == user_tmp:
                password = getpass.getpass(">>PassWord:").strip()
                if password == passwd_tmp:
                    print(">>欢迎登录购物车系，您的余额：%s元<<"%balance)
                    flag = False
                else:
                    print("用户名或密码错误，请重新输入。")
while True:
        print("你可买以下商品：")
        for i in products_list:
            print(id,i[0],i[1])
            id += 1
        choise = input(">>输入产品编号：").strip()
        if choise.isdigit():
            choise = int(choise)
            if choise >=1 and choise < id:
                p_name = products_list[choise-1][0]
                p_price = products_list[choise-1][1]
                if balance < p_price:
                    diff = p_price - balance
                    print("买不起%s，还差%s元"%(p_name,diff))
                else:
                    if p_name in bag[user_name]:
                        bag[user_name][p_name][1] += 1
                    else:
                        bag[user_name]=[p_name,1]
                    balance -= p_price
                    print("%s已经加入购物车"%p_name)
                    print("已经购买的商品：",bag[user_name],"余额%s"%balance)



        else:
            print("请输入正确的产品编号！")






