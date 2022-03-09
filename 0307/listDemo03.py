# 列表的方法（二）

# 列表元素的位置和词数
items = ['python','java','java','go','kotlin','python']
# 查找元素索引的位置
print(items.index('python'))
print(items.index('python',2))
# 错误的查询
# print(items.index('java',3)) #报错 ValueError: 'java' is not in list

print('-------------------------')

# 查询列表元素出现的词数
items = ['python','java','java','go','kotlin','python']
print(items.count('python'))
print(items.count('java'))
print(items.count('swfit'))

print('-------------------------')

# 元素的排列和反转
items = ['python','java','go','kotlin','python']
# 排序
items.sort()
print(items)
# 反转
items.reverse()
print(items)

print('-------------------------')

# 列表的生成式
# 使用for循环生成一个1-9的列表
items = []
for i in range(1,10):
    items.append(i)
print(items)
# 使用生成式生成一个1-9的列表
items = [x for x in range(1,10)]
print(items)

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items2 = []
for i in 'hello world':
    if i not in 'aeiou':
        items2.append(i)
print(items2)

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items2 = [x for x in 'hello world' if x not in 'aeiou']
print(items2)

'''
    Python中的列表底层是一个可以动态扩容的数组，列表元素在内存中也是连续存储的，所以可以实现随机访问,
    列表是容器，可以保存各种类型的数据，可以通过索引操作列表元素
'''
