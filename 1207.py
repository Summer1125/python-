import re
def addsub(s):
    num = re.findall("-?\d+\.?\d*",s)
    print(num)
    add = 0
    for i in num:
        i = float(i)
        print(i)
        add += i
    add = ("%.3f"%add)
    return add
    # symbol = re.findall("[+-]",s)
    # print(symbol)  
def repl(s):
    res = s.replace("+-","-")
    res = res.replace("++","+")
    res = res.replace("--","+")
    res = res.replace("-+","-")
    return res
def muldiv(s):#(2*3-1+6/2)
    print("mmmmmmmmm"+s)
    compu = re.search("-?\d+\.?\d*[*/]\d+\.?\d*",s)
    while compu != None:
        print(compu.group())
        num = re.findall("-?\d+\.?\d*",compu.group())
        print(num)
        symbol = re.search(r"[*/]",compu.group())
        print(symbol.group())

        if symbol.group() == "*":
            res = float(num[0]) * float(num[1])
        if symbol.group() == "/":
            res = float(num[0])/float(num[1])
        res = str(("%.2f"%res))
        print(res)

        s = s.replace(compu.group(),res)
        print(s)
        muldiv(s)
        return s
def del_barcket(s):
    res = re.search("\(-?\d+\.?\d*\)",s)
    print(res.group())
    num = re.search("-?\d+\.?\d*",res.group())
    print(num.group())
    s = s.replace(res.group(),num.group())
    print(s)
    return s

# del_barcket("(-8.9)")
s = "(2.4*3.0-1+6.6/2.2-3+(-8.4/4)-1*2*2+13/(4*2)/1)"
# print(muldiv(s))



s = "1-2*(60-30+(-40/5)*(9-2*5/3 + 7/3*99/4*2988+10*568/14)) - (-4*3)/(16-3*2)"

while re.search("\([^()]+\)",s):
    res = re.search("\([^()]+\)",s)
    print("---->"+res.group())

    muldiv = muldiv(res.group())

    s = s.replace(res.group(),muldiv)
    s = del_barcket(s)
    print("----->"+s)
    
# muldiv('(9-2*5/3 + 7/3*99/4*2988+10*568/14)')
