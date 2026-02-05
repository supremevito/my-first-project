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

    print(ret)

# cal(100)
# print("123123")
# cal(1000)
# cal(666)
cal(666,888)
cal(100,101)


def add(x,y):
    #x=1
    #y=2
    print(x+y)
add(1,2)
add(123456,256789)