"""
目录：
    1.位置参数
    2.关键字参数
    3.缺省参数
    4.不定长参数
        1.位置传递
        2.关键字传递
"""
"""
1.位置参数
    定义：
        调用时根据函数定义的参数位置来传递参数
    例如(语法):
        
        def user_info(name, age, gender):
            print(f"您的名字是{name}，年龄是{age}，性别是{gender}") 
        
        
        user_info("张三", 32, "男")    #调用(传入)函数
    
    注意：
        传递的参数和定义的参数的顺序及个数必须一致

2.关键字参数
    定义：
        关键字参数：函数调用时通过“键=值”形式传递参数.
        作用:可以让函数更加清晰、容易使用,同时也清除了参数的顺序需求. 
    例如(语法):
        
        def user_info(name, age, gender):
            print(f"您的名字是{name}，年龄是{age}，性别是{gender}") 
        
        
        user_info(name="张三", age=32, gender="男")    #调用(传入)函数
    注意：
         函数调用时,如果有位置参数时,位置参数必须在关键字参数的前面,且匹配参数顺序
         但关键字参数之间不存在先后顺序

3.缺省参数
    定义：
        缺省参数也叫默认参数,用于定义函数,为参数提供默认值,
        调用函数时可不传该默认参数的值(注意:所有位置参数必须出现在默认参数前，
        包括函数定义和调用）！！！默认值在最后面否则报错！！！！
    作用：
        当调用函数时没有传递参数，就会使用默认是用缺省参数对应的值
    例如(语法):
        
        def user_info(name, age, gender="男"):
            print(f"您的名字是{name}，年龄是{age}，性别是{gender}") 
        
        
        user_info(name="张三", age=30)    # gender没有传入参数
        user_info(name="张三", age=30, gender="女")    # gender有传入参数
    
4.不定长参数
    定义：
        不定长参数也叫可变参数.用于不确定调用的时候会传递多少个参数（不传参也可以）的场景
    作用：
        当调用函数时不确定参数个数时，可以使用不定长参数
    不定长参数的类型：
        1.位置传递
        2.关键字传递
    4.1.位置传递
        语法："*"后面的字符可以随便写，但是如果没有特殊要求，一般用args
            def user_info(*args):
                print(args) 
        
        
            user_info("小米", word, 123)    # 可以通过位置传递传入N个参数，
        注意：
            传进的所有参数都会被args变量收集,
            它会根据传进参数的位置合并为一个元组(tuple),
            args是元组类型,这就是位置传递
    4.2.关键字传递
         语法："**"后面的字符可以随便写，但是如果没有特殊要求，一般用kwargs
            def user_info(**kwargs):
                print(kwargs) 
        
        
            user_info(name="小米", age=13, )    # 可以通过关键字传递传入N个参数，
         注意：
            参数是“键=值”形式的形式的情况下,(满足字典键值对 'key=value' 这个形式)
            所有的“键=值”都会被kwargs接受,同时会根据“键=值”组成字典
"""


# 例1
# def user_info(name, age, gender):
#     print(f"您的名字是{name}，年龄是{age}，性别是{gender}")
#
#
# user_info("张三", 32, "男")  # 调用函数



# 例2
# def user_info(name, age, gender):
#     print(f"您的名字是{name}，年龄是{age}，性别是{gender}")
#
#
# user_info(name="张三", age=32, gender="男")  # 调用(传入)函数
#

# 例3
def user_info(name, age, gender="男"):
    print(f"您的名字是{name}，年龄是{age}，性别是{gender}")


user_info(name="张三", age=30)  # gender没有传入参数
user_info(name="张三", age=30, gender="女")   # gender有传入参数
