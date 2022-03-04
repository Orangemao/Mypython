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
# 删除指定索引位置的元素
items.pop(0)
items.pop(len(items) - 1)
print(items)

#清空列表中的元素
items.clear()
print(items)