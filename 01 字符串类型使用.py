# #字符串类型
# #本质上是一个序列 有序存储
# s = "hello yuan"
#
# #(1)获取字符操作 s[索引]
# print(s[1])
# print(s[4])
# print(s[9])
# print(s[-1])
# print(s[-2])
#
# #(2)切片操作 s[开始索引：结束索引] 顾 头不顾尾
# print(s[0:5])
# print(s[6:9])
# print(s[6:10])
# print(s[6:]) #结束索引不写就是默认到最后

# (3)f-str
name = "v"
age =18
s = f"敬爱的公司：我是{name}，我今年{age}岁，我对哈哈哈"
print(s)

#(4) 字符串内置方法
a = 100
s = "vito"
s2="vvvv"

print(s.upper())
print(s2.upper())
# print(a.upper())#就不要串类型 整型没有
s3="Hello Vito"
print(s3.upper())
print(s3.lower())


name = "副老师"
print(name.startswith("副")) #是不是以什么开头 ctrl键出来 可以看源码
print(name.endswith("哈")) #是不是以什么结尾
print(name.endswith("老师")) #是不是以什么结尾

s="北京 y广州 深圳 上海"
print(s.split(" ")) #['北京', '广州', '深圳', '上海']
#分割