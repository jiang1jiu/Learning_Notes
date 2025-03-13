"""

"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts,LabelOpts

# 打开美国的数据文件
f_us = open("折线图数据/美国.txt", "r", encoding="utf-8")
# 读取美国的全部数据
us_data = f_us.read()

# 打开日本的数据文件
f_jp = open("折线图数据/日本.txt", "r", encoding="utf-8")
# 读取日本的全部数据
jp_data = f_jp.read()

# 打开印度的数据文件
f_in = open("折线图数据/印度.txt", "r", encoding="utf-8")
# 读取印度的全部数据
in_data = f_in.read()

# 移除数据中的前导JSONP函数调用部分
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")

# 移除数据中的结尾括号
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# 将处理后的数据转换为字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 从一个包含美国疫情数据的字典中提取趋势数据
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 提取更新日期作为X轴数据，只取前314个数据点
us_x_Date = us_trend_data['updateDate'][:314]
jp_x_Date = jp_trend_data['updateDate'][:314]
in_x_Date = in_trend_data['updateDate'][:314]
# 提取疫情数据作为Y轴数据，这里选择第一种类型的疫情数据，并同样只取前314个数据点
us_y_Date = us_trend_data['list'][0]['data'][:314]
jp_y_Date = jp_trend_data['list'][0]['data'][:314]
in_y_Date = in_trend_data['list'][0]['data'][:314]

# 创建一个Line图表对象
line = Line()
# 将提取的日期数据添加到图表的X轴上
line.add_xaxis(us_x_Date)
# 将提取的疫情数据添加到图表的Y轴上，并命名为"美国22年疫情"    隐藏数字
line.add_yaxis("美国20年确诊人数", us_y_Date, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本20年确诊人数", jp_y_Date, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度20年确诊人数", in_y_Date, label_opts=LabelOpts(is_show=False))

# 设置全局配置选项，以定制图表的外观和行为
line.set_global_opts(
    # 设置标题配置项，包括标题文本、位置等
    title_opts=TitleOpts(title="20年美印日三国确诊人数对比折线图", pos_left="center", pos_bottom="1%"),
    # 设置图例配置项，决定是否显示图例
    legend_opts=LegendOpts(is_show=True),
    # 设置工具箱配置项，决定是否显示工具箱
    toolbox_opts=ToolboxOpts(is_show=True),
    # 设置视觉映射配置项，决定是否显示视觉映射
    # visualmap_opts=VisualMapOpts(is_show=True)
)
line.render()

f_in.close()
f_jp.close()
f_us.close()





