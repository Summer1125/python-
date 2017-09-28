menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
flag = True
while flag:
    for key in menu:
        print(key)
    choise = input(">:").strip()
    if len(choise) == 0:    continue
    if choise in menu:
        print('\n',menu[choise])

        while flag:
            for key2 in menu[choise]:
                print(key2)
            choise2 = input(">>:").strip()
            if len(choise2) == 0: continue
            if choise2 in menu[choise]:
                print('\n',menu[choise][choise2])
                while flag:
                    for key3 in menu[choise][choise2]:
                        print(key3)
                    choise3 = input(">>>：").strip()
                    if choise3 in menu[choise][choise2]:
                        print(menu[choise][choise2][choise3])
                        while flag:
                            for key4 in menu[choise][choise2][choise3]:
                                choise4 = input(">>>>:").strip()
                                if len(choise4) == 0:continue
                                if choise4 == "cd ..":
                                    break
                                if choise4 == "q":
                                    flag = False
                                    continue
                    elif choise3 == "cd ..":
                        break
                    elif choise3 == "q":
                        flag = False
            if choise2 == "cd ..":
                break
            if choise2 == "q":
                flag = False
    if choise == "q":
        flag = False




        
                
