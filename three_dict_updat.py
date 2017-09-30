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
last_layers = [ menu ]
current_layer = menu

while True:
    for key in current_layer:
        print(key)
    choise = input(">>>:").strip()
    if len(choise) == 0 :continue
    if choise in current_layer:
        last_layers.append(current_layer)
        current_layer = current_layer[choise]
    if choise == "b":
        if last_layers:
            current_layer = last_layers[-1]
            last_layers.pop()
    if choise == "q":
        break
