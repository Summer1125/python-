# python_basics
语法  学习过程中的笔记、练习

# three_dict_update.py 
三级字典练习，以及如何跳出三层循环
# loggin.py 
用户登录，密码输入三次以上则该用户锁定，对应文件locked_file.txt,uer_file.txt
# new_shopping_cart_bak.py
购物车程序，对应文件products.txt
# dispatch_errors.py
除错程序，根据一个error.txt文件，里面存的是出错的下标，来删除input.txt的坏道，重写文件为output.txt
# func_wrapper.py
有参装饰器的基本实现，原理是在给index()函数加上装饰器auth（）后，需要再在auth()的上一层定义auth2（）函数，返回auth，这个一样闭包，实现有参装饰器。
给index（）函数同时调用了两个装饰器，timmer和auth2,实现顺序是先执行auth2,在执行timmer。

认证功能需要在文件中读取用户名和密码，允许用户输入三次，存三次以上则锁定该用户，需要设置一个锁定文件来存取已经锁定的用户。
# generator.py
模拟LINUX中tail -f | grep "error"实时监控文件命令的生成器......实时监控文件，每写入一行，若输入的内容中包含“error”则输出到屏幕
# progress_help.py
协程函数基本语法，以及给它初始化一个next()功能的装饰器
# grep_func.py
生成器方法实现LINUX中grep筛选的功能
# gerator_list.py
生成器表达式的实现，将文件中的内容用生成器表达式的形式读取出来并保存成字典的形式，然后求和。求和函数调用可直接传一个迭代器进去。
