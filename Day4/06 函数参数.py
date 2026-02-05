#函数：组织代码
#功能：解耦和去重

"""
def poker():
    功能代码块


"""
#一个函数 没有参数 没有返回值 这个函数绝对不强大


def cal(m,n):
    #1+2+3..100 = 5050
    ret = 0
    #m=1
    for i in range(m,n+1):
        # print(i)
        ret+=i #ret = ret + i
    return ret #返回一份给调用者 可以理解成小秘书
    # print(ret)

# print(ret) #这里print ret会报错 因为上面函数结束后 ret就销毁了
print(cal(666,888)) #以上函数不return 就会返回None值

ret2 = cal(666,888) #也可以这样
print(ret2)



# # cal(100)
# # print("123123")
# # cal(1000)
# # cal(666)
# cal(666,888)
# cal(100,101)
#
#
# def add(x,y):
#     #x=1
#     #y=2
#     print(x+y)
# add(1,2)
# add(123456,256789)
