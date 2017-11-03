import datetime
#全局变量
file_path = 'atm.txt'
file_lock = 'atm_lock.txt'
all_info=[]
admin_info = {'name':'admin','password':'1234'}#管理员账号密码
msg1 = "---------------------ATM登陆系统---------------------\n\
    选择登录方式：\n\
        1、普通用户\n\
        2、管理员\n\
        3、退出\n\
-------------------------------------------------"
msg2 = "---------------------ATM用户系统---------------------\n\
    选择操作：\n\
        1: 存款\n\
        2: 取款\n\
        3: 还款\n\
        4: 转账\n\
        5: 打印账单\n\
        6: 退出\n\
-------------------------------------------------"
msg3 = "---------------------ATM管理系统---------------------\n\
    选择操作：\n\
        1: 冻结账户\n\
        2: 设置额度\n\
        3: 退出\n\
-------------------------------------------------"
current_login={'name':None,'status':False}
def is_time(func):
    '''装饰器，检查是否是15号'''
    def wrapper_time(*args,**kwargs):
        today = str(datetime.datetime.now())
        print(today)
        if today[8:10] == '15':
            res = func(*args,**kwargs) 
            return res
        else:
            print('~~~今天不出账单~~~')
    return wrapper_time
def loggin():
    '''普通用户认证登录'''
    count = 0
    while True:
        account = input(">>Account:").strip()
        with open(file_lock) as fp0:
            if account in fp0:
                print("**ERROR:该用户已被冻结，请联系管理员!")
                break
            else:
                for user in all_info:
                    if account == user['account']:
                        password = input('>>Password:').strip()
                        if password == user['password']:
                            while True:
                                print(msg2)
                                choise = input(">>选择业务：").strip()
                                if choise == '1':
                                    res = deposit(user)
                                elif choise == '2':
                                    res = with_drawal(user)
                                elif choise == '3':
                                    repayment(user)
                                elif choise == '4':
                                    trance(user,all_info)
                                elif choise == '5':
                                    put_bill(user)
                                elif choise == '6':
                                    print('~~~欢迎下次光临~~~')
                                    return 
                                else:
                                    print('**ERROR:输入有误')
                            # current_login['name'] = 'account'  ###更新目前的登录状态
                            # current_login['status'] = True
                            # return res
                        else:
                            print("**ERROR:用户名或密码错误")
                            count += 1
                if count == 3:
                    print('**ERROR:账号%s已经被冻结，请联系管理员！'%account)
                    frozen_user(account)
                    break
def with_drawal(user):
    '''取款'''
    money = int(input('>>取款金额：').strip())
    if user['balance'] < money:
        print('余额：%s'%user['balance'])
        if user['max'] < money:
            print('您的透支额度已经用完')         
        else:
            user['max'] -= money
            user['debt'] += money
            print('取款成功，可透支额度：%s 欠款%s'%(user['max'],user['debt']))  
    else:
        user['balance'] -= money
        print('取款成功，您的余额：%s'%user['balance'])
def deposit(user):
    '''存款'''
    money = int(input('>>存款金额：').strip())
    user['balance'] += money
    print('存款成功，您的余额：%s'%user['balance'])
def trance(user,all_info):
    '''转账'''
    account = input('>>对方账户：').strip()
    money = int(input('>>转账金额：').strip())
    if money > user['balance']:
        print('您的余额不足!')
    else:
        for dic in all_info:
            if dic['user'] == account:
                dic['balance']  += money
        user['balance'] -= money
        print('转账成功,您的余额：%s'%user['balance'])
def frozen_user(account):
    '''冻结账户'''
    with open(file_lock,'a') as fp:
        fp.write('\n'+account)
@is_time
def put_bill(user):
    '''出账单'''
    balance = user['balance']
    debt = user['debt']
    max_ = user['max']
    print('余额：%s   欠款：%s  最大透支额度：%s'%(balance,debt,max_))   
def repayment(user):
    '''还款'''
    if user['debt'] > 0:
        print('欠款：%s'%user['debt'])
        money = int(input(">>还款金额：").strip())
        user['debt'] -= money
        print('还款成功，还欠款：%s'%user['debt'])
    else:
        print('无欠款')
def admin():
    '''管理员添加账户，指定额度，冻结用户'''
    while True:
        name = input('>>管理员账户：').strip()
        pwd = input('>>管理员密码：').strip()
        if name == admin_info['name'] and pwd == admin_info['password']:
            while True:
                print(msg3)
                choise = input(">>输入操作：").strip()
                if choise == '1':
                    account = input(">>冻结账号：").strip()
                    frozen_user(account)
                    print('~~~操作成功~~~')
                if choise == '2':
                    account = input('>>输入账号：').strip()
                    max_ = input('>>可透支金额：').strip()
                    for dic in all_info:
                        if dic['account'] == account:
                            dic['max'] = max_
                            print('~~操作成功~~~')
                if choise == '3':
                    return
        else:
            print("**用户名或密码错误，重新输入")
def login_option():
    print(msg1)
    choise = input('>>登录方式：').strip()
    if choise == '2':
        admin()
    elif choise == '1':
        loggin()
    elif choise == '3':
        return
    else:
        print("输入有误！")



#调用
with open(file_path) as fp:
    for line in fp:
        dic = eval(str(line))
        # yield dic
        all_info.append(dic)
# for i in all_info:
#     print(i)
login_option()



 

