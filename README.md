# python_basics
语法  学习过程中的笔记、练习

# GuessAge.py 
# three_dict_update.py 
三级字典练习，以及如何跳出三层循环
# easy_test.py 
奇偶数求和，遍历打印
# loggin.py 
用户登录，密码输入三次以上则该用户锁定，对应文件locked_file.txt,uer_file.txt
# new_shopping_cart_bak.py
购物车程序，对应文件products.txt
# dispatch_errors.py
除错程序，根据一个error.txt文件，里面存的是出错的下标，来删除input.txt的坏道，重写文件为output.txt
# func_wrapper.py
有参装饰器的基本实现，原理是在给index()函数加上装饰器auth（）后，需要再在auth()的上一层定义auth2（）函数，返回auth，这个一样闭包，实现有参装饰器。
给index（）函数同时调用了两个装饰器，timmer和auth2,实现顺序是先执行auth2,在执行timmer。
