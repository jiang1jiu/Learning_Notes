"""

"""
"""
1.关于json
    可以理解为，就是python的字典
    或者是列表但是列表内部嵌套字典
2.python数据和json数据转化
    1.python转json    
        通过dumps()方法    将python列表或字典转换成json字符串
        例：
        import json   # 导入json模块
            json.dumps(dick)
    2.json转python
        通过loads()方法    将json字符串转换成python列表或字典
        例：
            json.loads(dick)
    3.解决中文编码问题
        传入一个ensure_ascii=False参数就可以解决了
        json.dumps(dick, ensure_ascii=False)    # 解决中文乱码
总结：
    1. json：
        是一种轻量级的数据交互格式，采用完全独立于编程语言的文本格式来存储和表示数据（就是字符串）
        Python语言使用JSON有很大优势，因为：JSON无非就是一个单独的字典
        或一个内部元素都是字典的列表所以JSON可以直接和Python的字典或列表进行无缝转换。
    2. json格式数据转化
        通过 json. dumps(data）方法把python数据转化为了 json数据
            data = json. dumps (data)
            如果有中文可以带上：
                ensure_ascii=False参数来确保中文正常转换
            通过 json. loads(data）方法把josn数据转化为了python列表或字典
                data = json. loads(data)
"""
