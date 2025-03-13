"""
"""
# 导入Line类，用于创建折线图
from pyecharts.charts import Line
# 从pyecharts库中导入图表配置项类
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 创建折线图对象
line = Line()
# 为line对象添加X轴标签
line.add_xaxis(["中国", "美国", "英国"])
# 为line对象添加Y轴数据
line.add_yaxis("GDP", [30, 40, 50])

# 设置全局配置项以优化图表展示效果
line.set_global_opts(
    # 设置标题配置项，包括标题文本、位置等
    title_opts=TitleOpts(title="GDP展示", pos_left="center",pos_bottom="1%"),
    # 设置图例配置项，决定是否显示图例
    legend_opts=LegendOpts(is_show=True),
    # 设置工具箱配置项，决定是否显示工具箱
    toolbox_opts=ToolboxOpts(is_show=True),
    # 设置视觉映射配置项，决定是否显示视觉映射
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 渲染图表，生成可视化结果
line.render()

"""
1.set_global_opts方法
    作用：
        进行全局配置选项，比如：标题、图例、工具箱、等公共的配置
"""

