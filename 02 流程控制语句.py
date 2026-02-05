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

