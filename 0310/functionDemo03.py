# 定义一个函数计算两数之和,并返回结果（不带参数值的 return 语句返回 None）
def nums(n,m):
    return n + m
print(nums(2, 3))

# isinstance判读是否是指定的类型
def sum(n,m):
    if not(isinstance(n,(int,float)) and isinstance(m,(int,float))):
        raise TypeError
    return n+m
print(sum(4,5))

# 函数也可以返回多个值，以元组的形式
def disvion(num1,num2):
    # 求商和余数
    a = num1 % num2
    b = (num1 - 1) / num2
    return a,b

print(disvion(33, 2),type(disvion(33,2)))

'''
    函数的参数
        主要的参数类型有：默认参数、关键字参数（位置参数）、不定长参数。
'''
# 默认参数 只有在形参表末尾的那些参数可以有默认参数值
def user_info(name,age,sex='男'):
    # 打印用户的信息
    print(f'姓名：{name}')
    print(f'年龄：{age}')
    print(f'性别：{sex}')

user_info('kang99',18)

