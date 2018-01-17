参考 ：http://www.cnblogs.com/guotianbao/p/6822174.html
# 模块与包
## 模块
    模块分三类：内置模块，第三方模块，自定义模块
    包是从文件夹的级别阻止模块
 ```python
    import 
    from ... import
 ```   
    只要是导入都会做以下三件事：
        1，执行文件
        2，创建名称空间
        3，创建模块名指向该文件的名称空间
            module.name的方式使用（模块名.名字）
 ```python
  import spam
    spam.name
 ```
 ```python
    from spam import name
    name
 ```
    
    
## 包的导入
     包是一通过使用‘.模块名’的方式来组织模块名称空间
     无论是import 还是from..import形式，凡是在导入语句中（而不是使用时）遇到带点的，都要第一时间提高警觉，这是关于包才有的导入语法。
     ！！！点的左边必须是包
        
        凡是导入包，都会执行包下面的__init__.py文件
        
        
        对于包来说，应该遵循以下原则：
            需要特别注意的是，可以用import导入内置或第三方模块，但是要绝对避免使用import来导入自定义的子模块，
            应该使用from...import...的绝对或者相对导入，且包的相对导入只能用from形式
        
