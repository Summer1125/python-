
# 元字符：.  ^  $  *  +  ?  { }  [ ]  |  ( )  \  共11个元字符
    ** 元字符： . 匹配任意字符
    ** 元字符： ^ 表示以什么开头
    ** 元字符： $ 表示以什么结尾
    ** 元字符： * 表示*号前面的字符可以出现0次到无穷次
    ** 元字符： + 表示+号前面的字符可以出现1次到无穷次
    ** 元字符：？ 表示？前面的字符可以出现[0,1]次
    ** 元字符：{}  可以在{}内自定义前面的字符出现的次数
    !!!注意：前面的*,+,?等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配
    ** 元字符：[ ] 是字符集，会匹配[ ]里边的所有字符，注意,除了^-/这3个符号外，其它字符都当做普通字符。
    ** 元字符：\ 反斜杠后边跟元字符去除特殊功能,比如\.   反斜杠后边跟普通字符实现特殊功能,比如\d

　　\d  匹配任何十进制数；它相当于类 [0-9]。
　　\D  匹配任何非数字字符；它相当于类 [^0-9]。
　　\s  匹配任何空白字符；它相当于类 [ \t\n\r\f\v]。
　　\S  匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
　　\w  匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
　　\W  匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]
　　\b  匹配一个特殊字符边界，比如空格 ，&，＃等
    
    ** 元字符：() 把()内的代码当做一个整体进行匹配
    ** 元字符：| 表示或的意思
# re 模块的常用方法
    import re
    #1
    re.findall('a','alvin yuan')        #返回所有满足匹配条件的结果,放在列表里

    #2
    re.search('a','alvin yuan').group()  #函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以
                                         # 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
     
    #3
    re.match('a','abc').group()     #同search,不过尽在字符串开始处进行匹配
     
    #4
    ret=re.split('[ab]','abcd')     #先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
    print(ret)#['', '', 'cd']
     
    #5
    ret=re.sub('\d','abc','alvin5yuan6',1)
    print(ret)#alvinabcyuan6
    ret=re.subn('\d','abc','alvin5yuan6')
    print(ret)#('alvinabcyuanabc', 2)
     
    #6
    obj=re.compile('\d{3}')
    ret=obj.search('abc123eeee')
    print(ret.group())#123 


    import re
    ret=re.finditer('\d','ds3sy4784a')
    print(ret)        #<callable_iterator object at 0x10195f940>
     
    print(next(ret).group())
    print(next(ret).group())
# 注意
    import re
 
    ret=re.findall('www.(baidu|oldboy).com','www.oldboy.com')
    print(ret)#['oldboy']     这是因为findall会优先把匹配结果组里内容返回,如果想要匹配结果,取消权限即可
     
    ret=re.findall('www.(?:baidu|oldboy).com','www.oldboy.com')
    print(ret)#['www.oldboy.com']




    import re

    print(re.findall("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>"))
    print(re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>"))
    print(re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>"))


    #匹配出所有的整数
    import re

    #ret=re.findall(r"\d+{0}]","1-2*(60+(-40.35/5)-(-4*3))")
    ret=re.findall(r"-?\d+\.\d*|(-?\d+)","1-2*(60+(-40.35/5)-(-4*3))")
    ret.remove("")

    print(ret)
