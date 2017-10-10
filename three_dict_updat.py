
# 三级菜单：
# 1. 运行程序输出第一级菜单
# 2. 选择一级菜单某项，输出二级菜单，同理输出三级菜单
# 3. 返回上一级菜单和顶部菜单
# 4. 菜单数据保存在文件中"
with open("Three_menu.txt") as fp:
    data = fp.read()
    menu = eval(data)
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
