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
import sys
import os
import getpass
count = 0
flag = True
shopping_bag = {}
users = "user_file.txt"
while True:
    user_name = input(">>UserName:").strip()
    password = getpass.getpass(">>PassWord:").strip()
    with open(users) as fp:
        for line in fp:
            user_tmp,passwd_tmp = line.split()
            