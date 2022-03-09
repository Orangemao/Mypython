'''
    合中的各个事物通常称为集合的元素。集合应该满足以下特性：
        无序性：一个集合中，每个元素的地位都是相同的，元素之间是无序的。
        互异性：一个集合中，任何两个元素都是不相同的，即元素在集合中只能出现一次。
        确定性：给定一个集合和一个任意元素，该元素要么属这个集合，要么不属于这个集合，二者必居其一，不允许有模棱两可的情况出现。

'''
# 创建集合
#   在Python中，创建集合可以使用{}字面量语法，{}中需要至少有一个元素，
#   因为没有元素的{}并不是空集合而是一个空字典

# 创建集合的字面量语法(重复元素不会出现在集合中)
set1 = {1,2,3,4,3,2}
print(set1)
print(len(set1))
# 创建集合的构造器语法(后面会讲到什么是构造器)
set2 = set('hello')
print(set2)