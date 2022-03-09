"""
    字符串的定义
    所谓字符串，就是由零个或多个字符组成的有限序列，把单个或多个字符用单引号或者双引号包围起来，就可以表示一个字符串

"""
s1 = "hello world"
s2 = 'ni hao'
print(s1,'\n',s2)
s3 = """
    hello
    world
"""
print(s3,end='')
print(s3)

# 转义字符和原始字符串
s1 = '\'hello,world!\''
print(s1)
s2 = '\\hello,world\\'
print(s2)

# 原始字符串
s1 = '\time up \now'
print(s1)
s2 = r'\time up \now'
print(s2)


# Python中还允许在\后面还可以跟一个八进制或者十六进制数来表示字符，
# 例如\141和\x61都代表小写字母a，前者是八进制的表示法，后者是十六进制的表示法。
# 另外一种表示字符的方式是在\u后面跟Unicode字符编码，例如\u9a86\u660a代表的是中文“骆昊”。

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u5eb7\u4e5d\u4e5d'
print(s1, s2)

"""
    字符串的运算
        Python为字符串类型提供了非常丰富的运算符，我们可以使用+运算符来实现字符串的拼接，
        可以使用*运算符来重复一个字符串的内容，可以使用in和not in来判断一个字符串是否包含另外一个字符串，
        我们也可以用[]和[:]运算符从字符串取出某个字符或某些字符。
"""
s1 = 'hello' + '\tworld'
print(s1)

s2 = 'hello' * 3
print(s2)

s3 = 'hello world'
print(s3[2])
print(s3[::2])

# 字符串的比较运算
s1 = 'a whole new world'
s2 = 'hello world'
print(s1 > s2)
print(s2 > s1)
print(s2 == 'hello world')
print(s2 == 'Hello world')
s3 = '康九九'
print(ord('康'),ord('九'))

print('-----------------------------------')

s1 = 'hello world'
s2 = 'hello world'
s3 = s2
# 比较字符串的内容
print(s1 == s2,s2 == s3)
# 比较字符串的内存地址
print(s1 is s2,s3 is s2)
print(id(s1),id(s2))

print('-----------------------------------')

# 获取字符串的长度
s = 'hello world'
print(len(s))
print(len('goodbye,world'))

# 成员运算
# Python中可以用in和not in判断一个字符串中是否存在另外一个字符或字符串，
# in和not in运算通常称为成员运算，会产生布尔值True或False。
s1 = 'hello world'
print('wo' in s1)
s2 = 'good bye'
print(s2 in  s1)
print(s2 not in s1)

"""
    索引和切片
    如果希望从字符串中取出某个字符，我们可以对字符串进行索引运算，运算符是[n]，其中n是一个整数，假设字符串的长度为N，那么n可以是从0到N-1的整数，
    其中0是字符串中第一个字符的索引，而N-1是字符串中最后一个字符的索引，通常称之为正向索引；在Python中，字符串的索引也可以是从-1到-N的整数，
    其中-1是最后一个字符的索引，而-N则是第一个字符的索引，通常称之为负向索引。注意，因为字符串是不可变类型，所以不能通过索引运算修改字符串中的字符。
"""
s = 'abc12345'
n = len(s)
print(n)
print(s[2:5]) # 要前面不要后面

print('-----------------------------------')

# 循环遍历每个字符
s1 = 'hello'
for i in s1:
    print(i)

for i in range(len(s1)):
    print(s1[i])
print('-----------------------------------')

# 字符串的方法
# 在Python中，我们可以通过字符串类型自带的方法对字符串进行操作和处理，
# 对于一个字符串类型的变量，我们可以用变量名.方法名()的方式来调用它的方法。
# 所谓方法其实就是跟某个类型的变量绑定的函数，后面我们讲面向对象编程的时候还会对这一概念详加说明。
s1 = 'hello world'
# 使用capitalize方法获得字符串首字母大写后的字符串
print(s1.capitalize())
# 使用title方法获得字符串每个单词首字母大写后的字符串
print(s1.title())
# 使用upper方法获得字符串大写后的字符串
print(s1.upper())

s2 = 'GOODBYE'
print(s2.lower())

print('-----------------------------------')

# 查找操作 如果想在一个字符串中从前向后查找有没有另外一个字符串，可以使用字符串的find或index方法。
s = 'hello world'
# find方法从字符串中查找另一个字符串所在的位置
# 找到了返回字符串中另一个字符串首字符的索引
print(s.find('wo'))
# 找不到返回-1
print(s.find('shift'))
# index方法与find方法类似
# 找到了返回字符串中另一个字符串首字符的索引
print(s.index('rld'))
# 找不到引发异常
# print(s.index('shift'))  # ValueError: substring not found

"""
    在使用find和index方法时还可以通过方法的参数来指定查找的范围，
    也就是查找不必从索引为0的位置开始。find和index方法还有逆向查找（从后向前查找）的版本，
    分别是rfind和rindex.
"""
s = 'hello world'
# 从前向后查找字符o出现的位置(相当于第一次出现)
print(s.find('0r'))

# 从索引为5的位置开始查找字符o出现的位置
print(s.find('o',5))

# 从后向前查找字符o出现的位置(相当于最后一次出现)
print(s.rfind('o'))

print('-----------------------------------')

"""
    性质判断
        可以通过字符串的startswith、endswith来判断字符串是否以某个字符串开头和结尾；
        还可以用is开头的方法判断字符串的特征，这些方法都返回布尔值，代码如下所示。
"""
s1 = 'hello world'
# startwith方法检查字符串是否以指定的字符串开头返回布尔值
print(s1.startswith('He'))
print(s1.startswith('hell'))
# endswith方法检查字符串是否以指定的字符串结尾返回布尔值
print(s1.endswith('ld'))

s2 = 'abc123456'
# isdigit方法检查字符串是否由数字构成返回布尔值
print(s2.isdigit())
# isalpha方法检查字符串是否以字母构成返回布尔值
print(s2.isalpha())
# isalnum方法检查字符串是否以数字和字母构成返回布尔值
print(s2.isalnum())

"""
    格式化字符串
        在Python中，字符串类型可以通过center、ljust、rjust方法做居中、左对齐和右对齐的处理。
        如果要在字符串的左侧补零，也可以使用zfill方法。
"""
s = "hello world"
# center方法以宽度20将字符串居中并在两侧填充
print(s.center(20,'*'))
# rjust方法以宽度20将字符串右对齐并在左侧填充空格
print(s.rjust(20,'*'))
# ljust方法以宽度20将字符串左对齐并在右侧填充~
print(s.ljust(20,'*'))
# 在字符串的左侧补零
print('22'.zfill(5))
print('33'.zfill(5))
print('1'.zfill(10))

"""
    修剪操作
        字符串的strip方法可以帮我们获得将原字符串修剪掉左右两端空格之后的字符串。
        这个方法非常有实用价值，通常用来将用户输入中因为不小心键入的头尾空格去掉，
        strip方法还有lstrip和rstrip两个版本.
"""
s = '   jackfrued@126.com  \t\r\n'
print(s)
print(s.strip()) # 去除左右空格
print(s.lstrip()) # 去除左空格
print(s.rstrip()) # 去除右空格

'''
    替换操作 如果希望用新的内容替换字符串中指定的内容，可以使用replace方法
           replace方法的第一个参数是被替换的内容，第二个参数是替换后的内容，
           还可以通过第三个参数指定替换的次数。
'''
s = 'hello world'
print(s.replace('o','@'))
print(s.replace('o','@',1))

'''
    拆分/合并操作
        可以使用字符串的split方法将一个字符串拆分为多个字符串（放在一个列表中），
        也可以使用字符串的join方法将列表中的多个字符串连接
'''
s = 'I love you'
word = s.split()
print(word)
print('#'.join(word))
print('kang'.join(s))
'''
    split方法默认使用空格进行拆分，我们也可以指定其他的字符来拆分字符串，
    而且还可以指定最大拆分次数来控制拆分的效果
'''
s = 'I#love#you#so#much'
words = s.split('#')
print(words)
words = s.split('#',3)
print(words)

print('-----------------------------------')

'''
    编码/解码操作
        Python中除了字符串str类型外，还有一种表示二进制数据的字节串类型（bytes）。
        所谓字节串，就是由零个或多个字节组成的有限序列。通过字符串的encode方法，
        我们可以按照某种编码方式将字符串编码为字节串，我们也可以使用字节串的decode方法，将字节串解码为字符串.
'''
a = '康'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b,c)
print(b.decode('utf-8'))
print(c.decode('gbk'))

"""
    简单的总结
            知道如何表示和操作字符串对程序员来说是非常重要的，因为我们需要处理文本信息，
            Python中操作字符串可以用拼接、切片等运算符，也可以使用字符串类型的方法。
"""
