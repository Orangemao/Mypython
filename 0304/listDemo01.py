"""
    定义和使用列表
        在Python中，列表是由一系元素按特定顺序构成的数据序列，这样就意味着定义一个列表类型的变量，可以保存多个数据，而且允许有重复的数据。
        列表也是一种结构化的、非标量类型，操作一个列表类型的变量，除了可以使用运算符还可以使用它的方法。
"""
# 列表元素的遍历
# 第一种方法
items = ['python','java','go','kotlin']
print(len(items))
for index in range(len(items)):
    print(items[index],index)

print('-----------------------------')

# 第二种方法
for item in items:
    print(item)

