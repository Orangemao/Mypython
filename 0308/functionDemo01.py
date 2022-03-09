'''
    输入m和n计算c(m,n)
    version: 0.1
    author: kang99
'''
# m = int(input('m='))
# n = int(input('n='))
# # 计算m的阶乘
# fm = 1
# for num in range(1,m+1):
#     fm *= num
# # 计算n的阶乘
# fn = 1
# for num in range(1,n+1):
#     fn *= num
# # 计算m-n的阶乘
# fk = 1
# for num in range(1,m-n+1):
#     fk *= num
# print(fm//fn//fk)

# 定义函数
def fok(m,n):
    return m + n
print(fok(2,3))

# 函数的参数
# 参数的默认值
"""
    参数的默认值
    version: 0.1
    author: kang99
"""
from random import randint
# 定义摇色子的函数，n表示色子的个数，默认值为2
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total
# 如果没有指定参数，那么n使用默认值2，表示摇两颗色子
print(roll_dice())
# 传入参数3，变量n被赋值为3，表示摇三颗色子获得点数
print(roll_dice(3))

def add(a=0,b=0,c=0):
    # 三个数相加求和
    return a+b+c
print(add(2,3,3))

# 传递参数时可以不按照设定的顺序进行传递，但是要用“参数名=参数值”的形式
print(add(c=50,a=22,b=44))
'''
    注意：带默认值的参数必须放在不带默认值的参数之后，否则将产生SyntaxError错误，
    错误消息是：non-default argument follows default argument，
    翻译成中文的意思是“没有默认值的参数放在了带默认值的参数后面”。
'''
