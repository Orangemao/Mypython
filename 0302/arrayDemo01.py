print('hello world')
print('goodbye world')

# python分支循环学习
"""
    用户身份验证
    version：1.0
    author：kang99
"""
username = input("请输入用户名")
password = input("请输入密码")

if username == "kang99":
    if password == "123":
        print("登录成功")
    else:
        print("登录失败")
else:
    print("用户名错误，请重新输入")

print('------------分隔符-------------')

"""
    用户身份验证
    version:2.0
    author: kang99
"""
username = input("请输入用户名")
password = input("请输入密码")

if username == "kang99" and password == '123':
    print("登录成功")
else:
    print('登录失败')

