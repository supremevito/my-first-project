# 一、基本数据类型
# 字符串 "" ''
# 数字 1 2 3
# 布尔类型 Ture False

# 二、高级数据类型
# 列表 []
# 字典 {}

'奥说'

# print(1 + 2)
# print(1 - 2)
# print(1 * 2)
# print(1 / 2)

#Ctrl + D
#Ctrl + /

# a=1
# b=2
#
# # 用变量代指常用的值
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)


# print(100)
# x =100
# print(x)

#用不用变量 开拓空间 取决于你后面还用不用 这个100
#Python 执行原理：从上到下，每行依次有且只有执行一次
#（2）变量怎么变？
level =1
print(level)

#省略：闯关成功，登记加一
level = 1 + 1
print(level)
#python跟c/c++不一样 python变量重新赋值是开一个新创建的数据空间 然后重新指向这个新的空间
# 把原来空间垃圾回收了 python所有的空间都不能改

#（3）变量的表达式赋值
coin =100

#打死个妖怪，奖赏10个金币

coin = coin + 10
#变量的重新赋值
#金币的累加
print(coin)

#（4）变量的命名要规范
# --规范见名知意
# l=1
#level =2
#等级 = 3
#等级 = 等级+1
#print(等级)

# -- 变量名只能包含字母、数字和下划线_,不能以数字开头
#a2= 8

# --变量名不能使用保留字(例如f、else、while等)
#print = 2
#print(print)