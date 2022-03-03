import  random

f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
for index in range(6000):
    face = random.randint(1,6)
    if face == 1:
        f1 += 1
    elif face ==2:
        f2 += 1
    elif face == 3:
        f3 += 1
    elif face == 4:
        f4 += 1
    elif face == 5:
        f5 += 1
    else:
        f6 += 1
print(f'1点出现了{f1}次')
print(f'2点出现了{f2}次')
print(f'3点出现了{f3}次')
print(f'4点出现了{f4}次')
print(f'5点出现了{f5}次')
print(f'6点出现了{f6}次')

print('_________________________')

items1 = [35,12,99,68.55,87]
items2 = ['python','java','go','kotlin']
items3 = list(range(1,10))
print(items3)
print(items2)
print(items1)
items4 = list('hello')
print(items4)

# 列表是一种可变的数据类型，不同与str类型，str是以一种不可变的数据类型，也就是说对字符串做拼接、
# 重复、转换大小写、修剪空格等操作的时候会产生新的字符串、原来的字符串并没有发生任何改变

print('_________________________')

"""
    列表的运算符号：
        列表和字符串数据类型一样、列表也支持、重复、成员运算、索引和切片以及比较运算
"""
item10 = [35,12,99,68,55,87]
item20 = [45,8,29]

# 列表的拼接
item30 = item10 + item20
print(item30)
# 列表的重复
item40 = ['hello']*3
print(item40)
# 列表成员的运算


