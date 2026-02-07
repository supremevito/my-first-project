# # # s="北京 广州 深圳 上海"
# # #编程本质就是对数据做各种操作
# # #基本数据基本操作
# # #高级数据（容器数据）增删改查操作
# # #这里面有几个城市
# # # print(len(s));
# #
# #
# # #列表语法:[元素1,元素2,元素3...] 放什么都行
# # #元素个数理论上没有限制
# # #元素值可以是任意类型，包括数字、字符串、列表、字典
# # #元素是从左到右有序存储
# # l = ["北京","天津","哈尔滨","乌鲁木齐"]
# # #只要是有序存储就可以做索引操作
# # print(len(l))
# #
# # #一、基本语法：查（基本语法实现）
# # # #(1)索引操作 l[索引]
# # print(l[1])
# # print(l[-1])
# #
# # # #(2)切片操作 l[开始索引:结束索引] 顾头不顾尾
# # print(l[0:])
# # print(l[0:3])
# # print(l[:]) #前面不写也默认是0
# # print(l[-3:])
# #
# # #内置方法：增删改
# #
# # #二、改（基本语法实现）
# # l = ["北京","天津","哈尔滨","乌鲁木齐"]
# # print(l[1])
# # l[1] = "广州"
# # print(l)
# #
# # #增：内置方法 列表对象.方法()    append insert extend
# # gf_list = ["范冰冰","刘亦菲","桃谷"]
# # # print(len(gf_list))
# # # gf_list.append("赵丽颖")
# # # print(gf_list)
# # #按顺序追加的
# # gf_list.insert(0,"章若楠")
# # print(gf_list)#建议用append 不用insert 因为性能差
# #
# #
# # #删：内置方法：remove pop clear
# #
# # gf_list.remove("刘亦菲")#按元素值删除
# # print(gf_list)
# #
# # gf_list.pop(0)#按索引值删除
# # print(gf_list)
# # gf_list.pop(-1)#按索引值删除
# # print(gf_list)
# #
# # gf_list = ["范冰冰","刘亦菲","桃谷"]
# # print(gf_list)
# # gf_list.clear()#全删掉 光剩一个空列表
# # print(gf_list)
# #
#
# #列表与for循环
# gf_list = ["范冰冰","刘亦菲","桃谷","铃"]
# # for i in gf_list: #遍历循环 for循环
# #     print("hello")
# #     # print(i)
# #     # pass #pass就是什么都不干
#
# for gf in gf_list: #遍历循环 for循环 gf是遍历的元素值
#     # print("hello")
#     print(f"我的宝贝：{gf},我太好了")
#     # print(gf)
#     # pass #pass就是什么都不干
#
#
# l = [23,14,2,11,5]
#
# l2 = []
# for i in l:
#     print(i*i)
#     l2.append(i*i)
# print(l2)
#

#range()函数 生成几到几的一个列表

# for i in [1,1,1,1,1]:
#     print("hello v")
#
# for i in range(1,11):
#     print(i)

for i in range(100): #前面不写就是从0开始
    print(i)
