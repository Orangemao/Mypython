"""
    打印乘法口诀表
    version: 0.1
    author: kang99
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}',end='\t')
    print()

print('_______________________________')

"""
    输入一个正整数判断它是不是素数
    version: 0.1
    author: kang99
"""
num = int(input("请输入一个正整数"))
end = int(num ** 0.5)
is_prime = True
for x in range(2,end+1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')

print('__________________________________')

"""
    输入两个正整数，计算他们最大的公约数和最小公倍数
    version: 1.0
    author: kang99
"""
x = int(input('x ='))
y = int(input('y ='))
for factor in range(x,0,-1):
    if x % factor == 0 and y % factor == 0:
        print(f'{x}和{y}的最大公约数是{factor}')
        print(f'{x}和{y}的最小公倍数是{x * y // factor}')
        break