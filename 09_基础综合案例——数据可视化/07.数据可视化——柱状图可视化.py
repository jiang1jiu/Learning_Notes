# 导入Bar类，用于创建柱状图
from pyecharts.charts import Bar
from pyecharts.options import *
# 实例化Bar类，创建一个柱状图对象
bar = Bar()
# 添加柱状图的x轴数据
bar.add_xaxis((["中国", "美国", "英国"]))
# 添加柱状图的y轴数据，标签为"GDP"，数据分别为30, 20, 10
bar.add_yaxis("GDP", [30, 20, 10],label_opts=LabelOpts(
    position="right"
))
# 调用reversal_axis方法，翻转x轴和y轴
bar.reversal_axis()
# 调用render方法，将柱状图渲染为HTML文件
bar.render("中美英三国的GDP柱状图.html")
