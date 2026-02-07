#编程本质就是对数据做各种操作
#基本数据基本操作
#高级数据（容器数据）增删改查操作

# #列表的灵魂是索引管理值
# info = ["v",18,185,100]
# print(info[2])
# #字典 没有索引 但是是连续的 hash 怎么存就怎么查
# #字典的灵魂是键管理值
# info2 = {"name":"v","age":18,"height":185,"weight":100}
# #一、基本语法实现
# #（1）查
#
# print(info2["height"])
# #增和改
# #（2）添加和修改
# info2["gender"] = "male"
# #你没有就会添加 有就修改
# print(info2)
# info2["age"] = 20
# print(info2)
# #（3）删除键值对
# del info2["name"] #del什么都能删
# print(info2)
# # del info2

#二、内置函数实现(推荐，但是上面的也要会) ：字典对象.方法()
info2 = {"name":"v","age":18,"height":185,"weight":100}

#（1）查
# print(info2["name"])
print(info2.get("name"))
#（2）添加和修改
info2.update({"name":"vi","age":22,"gender":"female"})
print(info2)
#（3）删除键值对
info2.pop("weight")
print(info2)


#二、内置函数实现
