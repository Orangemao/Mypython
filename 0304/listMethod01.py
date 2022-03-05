# 列表的方法
items = ['python','java','go','kotlin']
# 使用append方法在尾部添加元素
items.append('swift')
print(items)
# 使用isert方法在列表指定索引位置插入元素
items.insert(2,'sql')
print(items)

# 删除指定元素
items.remove('java')
print(items)
# 删除指定索引位置的元素,pop会返回一个指定删除元素
one = items.pop(0)
items.pop(len(items) - 1)
print(items)
print(one)

#清空列表中的元素
items.clear()
print(items)

print('--------------------------')

# 使用del关键字
itemone = ['python','java','go','kotlin']
del itemone[1]
print(itemone)