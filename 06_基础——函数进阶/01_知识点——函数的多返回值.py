"""

"""
"""
1.多返回值的代码格式
    语法：
        def test_return():
            return 返回值1, 返回值2
        
        x，y = test_return()
        print(x)     结果1
        print(y)     结果2
    
    按照返回值的顺序，写对应的多个变量接收即可
    变量之间用逗号隔开
    支持不同类型的数据return
"""


# 例子
def test_return():
    return 1, 2, "hello", {1, 2, 3}


x, y, z, p = test_return()
print(x)  # 结果1
print(y)  # 结果2
print(z)  # 结果2
print(p)  # 结果2
