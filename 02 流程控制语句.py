#(1) 顺序语句
print("hello vito")
print(1 + 2)
print(3 > 5)

#(2)分支语句
"""
if 表达式：
    表达式为真执行的语句
else:
    表达式为假执行的语句
"""
age = 19

if age >= 18:
    print("成年")
    print("亚洲")
    print("欧美")
    print("日韩")
else:
    print("未成年")
    print("天线宝宝")
    print("黑猫警长")
print("大头儿子")
print("Gameover")
#嵌套不要超过三层

"""
    js/Java/C/C++/Go
    if (age >=18){
    print("成年")
    print("亚洲")
    print("欧美")
    print("日韩")}
else{
    print("未成年")
    print("天线宝宝")
    print("黑猫警长")
}
"""

#(3)循环语句  for：遍历循环  while:条件循环

print("Hello Yuan")
"""
while 表达式：
    循环体语句
    
while(表达式){
    循环体语句
}
"""

# while 2>1:
#     print("hello 1")
#     print("hello 2")
#     print("hello 3")

#有限循环
n = 0
while n <= 100:
    print("hello",n)
    n += 1

print("游戏结束")



#基本数据类型跟高级数据类型区别 就是 能不能拆开
#比如说数字10就拆不了
#本质上字符串是高级数据类型（类似一个容器） 但是大家愿意把它扔在基本数据类型里面
#主要是因为它只能做字符存储 存不了更高级的数据类型 如布尔
#编程的本质就是在操纵数据 基本数据类型就upper and lower
#高级数据类型就增删改查