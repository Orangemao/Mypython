# 输出语句
#   1.默认print会在末尾自动加上换行符
#   2.如果不想换行可以在末尾加上 end = ""
#   3.可以在end = '' ''中加入字符串

print('hello world')
print('测试不换行',end='')
print('测试不换行')

# 测试在end = '' 中加入字符串
print('today',end=',')
print('one',end='.')
print()

# 输入
get_input = input("please input your text")
print("得到输入的内容%s" %get_input)

# python文件命名方式
# 用拼音或者英文字母

# 练习题
# 1．使用print输出自己的姓名
# 2．使用print输出
#   春眠不觉晓，
#   出处闻啼鸟，
#   夜来风雨声，
#   花落知多少。
# 3．是用print输出
#   春眠不觉晓,出处闻啼鸟，夜来风雨声，花落知多少。

# 1
print('kangkan')
# 2
print("春眠不觉晓",end=',')
print("出处闻啼鸟",end=',')
print("夜来风雨声",end=',')
print("花落知多少",end='。')

print('hell world')
print('hello world')