""""""
"""
1.追加写入 a模式
    语法：
        f = open('name','a')   #新建文件，打开方式为‘a’追加
        f.write(追加内容)        #通过 write()方法追加内容
        f.flush()  / f.close()    #内容刷新，只有调用flush方法（或者关闭文件）才会真正的写入文件
    注意：
        a模式，文件不存在会创建文件
        a模式，文件存在会在原有内容后面，追加写入文件
"""
f = open("文件/test3.txt", "a", encoding="utf-8")
f.write("我是原来的内容")
f.write("\n我是追加的内容")
f.flush()
