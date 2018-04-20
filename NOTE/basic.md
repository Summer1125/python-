# 集合的增删改查

  -	a.update(b)  将b并到a，a的内容发生变化
  -	a.clear()
  -	a.add("FF")		增加一个不存在的元素
  -	a.copy()		复制
  -	a.difference_update(b)		求差之后合并到a
  -	a.discard("aa")		删除
  -	a.pop()			随机删除
  -	a.remove("aa")	删除，与discard与区别，如果元素不存在会报错，discard不会报错	
  -	a.issubset(b)	判断a是否是b的子集，返回True或False
  -	a.issuperset(b)	判断a是否是b的父集


# 字符串的操作（eg.name="aaaexaea"）

  -	name.capitalize()	首字母大写
  -	name.casefold()		大写转换成小写
  -	name.center(50,"*")	
  -	name.count("e",3，7)	统计在3到7之间有几个e	
  -	name.endwith("l")	以l结尾
  -	name.expandtabs(3)	 设置tab键的长度
  -	name.find("e")		查询，找不到返回-1，可以在后面接着定义查询的位置("e",3,7)
  -	name.format()		格式化输出
  -	name.format_map()
  -	name.index("ex")	返回索引值
  -	name.isanum()
  -	name.isdecimal()	判断是否是正整数
  -	name.isalpha()		是否是字母
  -	name.is adentifier()判断是否是合法变量名
  -	name.islower()		是否小写
  -	name.isupper()		是否大写
  -	name.issapce()		是否是空格
  -	name.istitle()		是不是英文标题
  -	name.join()			将列表拼成字符串
  -	name.ljust(50,"-")	左对齐，不够的补“-”
  -	name.lower()		大写变小写
  -	name.lstrip()		移除左边的换行、tab键，空格，也可指定
  -	name.split()
  -	name.swapcase()		大小写交换
  -	nama.translate()	字符翻译
  -	name.replace("a","A",1) 替换一次


# 常用：

  -	strip
  -	center
  -	count
  -	find
  -	casefold/lower/upper
  -	join
  -	split
  -	endwith/startwith
  -	replace
  -	index
