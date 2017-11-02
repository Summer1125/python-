import datetime
#全局变量
file_path = 'atm.txt'
file_lock = 'atm_lock.txt'
all_info=[]
msg1 = "---------------------ATM系统---------------------\n\
    选择登录方式：\n\
        1、普通用户\n\
        2、管理员\n\
-------------------------------------------------"
msg2 = "---------------------ATM系统---------------------\n\
    选择操作：\n\
        1、存款\n\
        2、取款\n\
        3、还款\n\
        4、打印账单\n\
-------------------------------------------------"
current_login={'name':None,'status':False}
# def is_time(func):
#     '''装饰器，检查是否是15号'''
#     def wrapper_time(*args,**kwargs):
#         today = datetime.datetime.now()
#         print(today)
#         if today[8:10] == '15':
#             res = func(*args,**kwargs) 
#             return res
#     return wrapper_time
    
def with_drawal(account):
    '''取款'''
    
def deposit():
    '''存款'''
    pass
def trance():
    '''转账'''
    pass
def frozen_user(account):
    '''冻结账户'''
    with open(file_lock,'a') as fp:
        fp.write('\n'+account)

def loggin(all_info):
    '''普通用户登录'''
    count = 0
    while True:
        account = input(">>Account:").strip()
        with open(file_lock) as fp0:
            if account in fp0:
                print("**ERROR:该用户已被冻结，请联系管理员!")
                break
            else:
                for user in all_info:
                    if account == user['user']:
                        print(type(user['password']))
                        password = input('>>Password:').strip()
                        print(type(password))
                        if password == user['password']:
                            print(msg2)
                        else:
                            print("**ERROR:用户名或密码错误")
                            count += 1
                if count == 3:
                    print('**ERROR:账号%s已经被冻结，请联系管理员！'%account)
                    frozen_user(account)
                    break

def put_bill():
    '''出账单'''
    pass
def repayment():
    '''还款'''
    pass
def add_usr():
    '''管理员添加账户，指定额度，冻结用户'''
    pass



with open(file_path) as fp:
    for line in fp:
        dic = eval(str(line))
        all_info.append(dic)
for i in all_info:
    print(i)
loggin(all_info)
