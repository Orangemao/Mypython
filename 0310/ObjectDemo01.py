'''
    面向对象


'''

# 属性
class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

kang99 = Person('kang99',19,'男')
print(kang99,"\t",kang99.__dict__)
print(kang99.name)

print('----------------------------------------')

class Dog:
    def __init__(self,name,blood,aggr,kind):
        self.name = name
        self.blood = blood
        self.aggr = aggr
        self.kind = kind

xiaobai = Dog('小白',2500,249,'柴犬')
print(xiaobai.name)
print(xiaobai.__dict__)

# 方法
