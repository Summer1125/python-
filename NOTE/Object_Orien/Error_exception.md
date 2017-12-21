
# 异常处理
  分成两种：
    一种是由语法上的错误引起的异常，另一种是逻辑上的错误引发的异常。
    前者应该在程序执行前就改成，后者尽量使用if来预防，对于逻辑上的错误，无法预知错误什么时候发生的时候应该用try...except处理。
    
# 语法：
      try:
        被检测的代码块
       except 异常类型 as e:
        print(e)
       except 异常类型 as s:
        print(e)
       except Exception as e:
        pass
       else:
        没有异常触发
      finally:
        有没有异常都出发
# 自定义异常
  class Myexception(BaseException):
    pass
  
  
# 主动触发异常：
  raise Type("异常值")
# 断言
  assert 1==2
