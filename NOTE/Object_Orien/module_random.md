# radonm模块
    >>> random.random()             #0到1之间的浮点数
    >>> random.randint(1,10)        #[1,10]之间的整数
    >>> random.randrange(1,5)       #[1,5)之间的整数
    >>> random.choice([1,2,3,4])    #[1,2,3,4]列表中随机一个数
    >>> random.sample([1,2,3,4,5],2)#[1,2,3,4,5]列表中随机选两个数
    >>> random.uniform(1,3)         #(1,3)之间随机小数

    >>>item=[1,2,3,4,5,6]
        random.shuffle(item)
        print(item)                 #将item打乱顺序

## 随机生成5个含有数字和字母的验证码
    def validate():
        s = ''
        for i in range(5):
            num = random.randint(0,9)
            upper_alph = chr(random.randint(65,90))
            lower_alph = chr(random.randint(97,122))

            ret = random.choice([str(num),upper_alph,lower_alph])
            s += ret
        return s
    print(validate())
