"""
    元组的应用场景
    1.打包和解包
    当我们把多个用逗号分隔的值赋给一个变量时，多个值会打包成一个元组类型；
    当我们把一个元组赋值给多个变量时，元组会解包成多个值然后分别赋给对应的变量
        注意：1.）在解包时，如果解包出来的元素个数和变量个数不对应，会引发ValueError异常，
                错误信息为：too many values to unpack（解包的值太多）或not enough values to unpack（解包的值不足）。
             2.）有一种解决变量个数少于元素的个数方法，就是使用星号表达式，我们之前讲函数的可变参数时使用过星号表达式。
                有了星号表达式，我们就可以让一个变量接收多个值，代码如下所示。需要注意的是，用星号表达式修饰的变量会变成一个列表，
                列表中有0个或多个元素。还有在解包语法中，星号表达式只能出现一次。
    2.交换两个变量的值
    交换两个变量的值是编程语言中的一个经典案例，在很多编程语言中，
    交换两个变量的值都需要借助一个中间变量才能做到，如果不用中间变量就需要使用比较晦涩的位运算来实现。
"""
# 打包和解包
a = 10,20,30
print(type(a),a)

j,k,l = a
print(j,k,l)

a = 1,10,100,1000
i,j,*k = a
print(i,j,k)
i,*j,k = a
print(i,j,k)
*i,j,k = a
print(i,j,k)
*i,k = a
print(i,k)
i,j,k,*l = a
print(i,j,k,l)
i,j,k,l,*m = a
print(i,j,k,l,m)
# 需要说明一点，解包语法对所有的序列都成立，这就意味着对列表以及我们之前讲到的range函数返回的范围序列都可以使用解包语法。
a,b,*c = range(1,10)
print(a,b,c)
a, b, c = [1, 10, 100]
print(a, b, c)
a,*b,c = 'hello'
print(a,b,c)

# 交换两个变量的值
a = 20
b = 30
a,b = b,a
print(a,b)
print("------------------------------------")

"""
    元组和列表的比较
     1.元组是不可变类型，不可变类型更适合多线程环境，因为它降低了并发访问变量的同步化开销。
       关于这一点，我们会在后面讲解多线程的时候为大家详细论述。
     2.元组是不可变类型，通常不可变类型在创建时间和占用空间上面都优于对应的可变类型。
"""
import sys
import timeit

a = list(range(100000))
b = tuple(range(100000))
print(sys.getsizeof(a),sys.getsizeof(b))

print(timeit.timeit('[1,2,3,4,5,6,7,8,9]'))
print(timeit.timeit('(1,2,3,4,5,6,7,8,9)'))

print('------------------------------------')

# Python中的元组和列表是可以相互转换的，我们可以通过下面的代码来做到。
# 将元组转换成列表
info = ('kang99',188,True,'shanghai')
print(list(info))
# 将列表转化成元组
fruits = ['apple','banana','orange']
print(tuple(fruits))

"""
    总结：
    列表和元组都是容器型的数据类型，即一个变量可以保存多个数据。列表是可变数据类型，
    元组是不可变数据类型，所以列表添加元素、删除元素、清空、排序等方法对于元组来说是不成立的。
    但是列表和元组都可以进行拼接、成员运算、索引和切片这些操作。推荐使用用列表的生成式语法来创建列表
"""