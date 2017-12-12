import re
def muldiv(s):#求乘除
    compu = re.search("-?\d+\.?\d*[*/]-?\d+\.?\d*",s)
    
    num = re.findall("-?\d+\.?\d*",compu.group())
    symbol = re.search(r"[*/]",compu.group())
    # print(num,symbol.group())
    if symbol.group() == "*":
        res = float(num[0]) * float(num[1])
    if symbol.group() == "/":
        res = float(num[0])/float(num[1])

    res = str(("%.2f"%res))
    s = s.replace(compu.group(),res)
    # print('--====',s)
    if(re.search("-?\d+\.?\d*[*/]\d+\.?\d*",s) == None):
        # print('rrrrrrrrrrr',s)
        return s
    else:
        return muldiv(s)
def addsub(s):#加减法
    num = re.findall("-?\d+\.?\d*",s)
    print(num)
    if num != None:
        # print(num)
        add = 0
        for i in num:
            i = float(i)
            print(i)
            add += i
        add = ("%.3f"%add)
        print("++++++",add)
        return add
    else:
        return s
def repl(s):#替换符号
    res = s.replace("+-","-")
    res = res.replace("++","+")
    res = res.replace("--","+")
    res = res.replace("-+","-")
    return res


s = "1-2*(60-30+(-40/5)*(9-2*5/3+7/3*99/4*2988+10*568/14))-(-4*3)/(16-3*2)"
# s = "(9-2*5/3 + 7/3*99/4*2988+10*568/14))"

while re.search("\([^()]+\)",s):
    s_list = re.findall("\([^()]+\)",s)
    for i in s_list:
        md= muldiv(i)
        ad = addsub(md)
        s = s.replace(i,ad)
        s = repl(s)
        ss = muldiv(s)
        print(ss)
        
   
# while re.search("\([^()]+\)",s):
#     res = re.search("\([^()]+\)",s)
#     if res != None:
#         md= muldiv(res.group())
#         s = s.replace(res.group(),md)
