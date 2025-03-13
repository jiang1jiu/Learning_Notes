"""
题目：
    有一份账单文件bill.txt,记录了消费收入的具体记录
要求：
    读取文件
    将文件写出到bill. txt. bak文件作为备份
    同时,将文件内标记为测试的数据行丢弃
"""
fr = open("文件/bill.txt", "r", encoding="utf-8")
fw = open("文件/bill.txt.bak", "w", encoding="utf-8")
for line in fr:
    if line.count("测试"):
        continue
    else:
        fw.write(line)
fr.close()
fw.close()
