"""
    用for循环实现1-100求和
    version: 1.0
    author: kang99
"""

total = 0
for a in range(1,101):
    total += a
print(total)

print('-----------分割符------------')

"""
    用for循环实现1-100之间的偶数求和
    version: 0.1
    author: kang99
"""

two = 0
for a in range(2,101,2):
    two += a
print(two)

print('--------------------------')

"""
    while循环,猜数字游戏
    version: 1.0
    author: kang99
"""
import random
# 产生一个1-100范围的随机数
answer = random.randint(1,101)
counter = 0
while True:
    counter += 1
    number = int(input("请输入："))
    if number < answer:
        print("大一点")
    elif number > answer:
        print("小一点")
    else:
        print("恭喜你猜对了")
        break
print(f'你总共猜了{counter}次')