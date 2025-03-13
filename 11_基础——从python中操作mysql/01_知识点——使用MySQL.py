from pymysql import Connection

# 创建与MySQL数据库的连接
connection = Connection(
    host="localhost",  # 主机名（ip）
    port=3306,         # 端口
    user="root",       # 用户名
    password="root",   # 密码
    autocommit=True    # 自动提交   这个和下面那个2选1
)
"""
1.基础使用
"""
# # 创建游标对象
# cursor = connection.cursor()
#
# # 选择数据库
# connection.select_db("demo")
#
# # # 执行SQL语句：创建名为test_pymysql的表
# # cursor.execute("create table test_pymysql(id int)")
#
# # 执行SQL查询以获取学生表中的所有记录
# cursor.execute("SELECT * FROM student")
#
# # 获取并存储查询结果中的所有行
# results = cursor.fetchall()
#
# # 打印查询结果
# print(results)
#
# # 关闭数据库连接
# connection.close()

"""
2.数据插入
"""
# # 创建游标对象
# cursor = connection.cursor()
#
# # 选择数据库
# connection.select_db("demo")
#
# # 插入学生信息到数据库
# cursor.execute("INSERT INTO student (id,name, age) VALUES (3,'小段',20);")
#
# # 提交事务，确保数据写入数据库  和上面的二选一
# connection.commit()
#
# # 关闭数据库连接
# connection.close()





















