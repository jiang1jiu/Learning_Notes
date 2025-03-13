from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 创建Map类实例，用于绘制地图
map = Map()

# 定义地图数据，格式为(地区名称, 数值)
data = [
    ("北京市", 99),
    ("上海市", 199),
    ("河南省", 207),
    ("河北省", 2344),
    ("湖南省", 9)
]

# 向地图中添加数据，"测试地图"是图例名称，data是地图数据，"china"指定地图范围为中国
map.add("测试地图", data, "china")

# 设置地图的全局配置项，包括视觉映射配置
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 显示视觉映射配置项
        is_piecewise=True,  # 将视觉映射配置为分段形式
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#ccffff"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#990033"},
            {"min": 1000, "max": 9999, "label": "1000-9999", "color": "#33FF33"}
        ]
    )
)



# 渲染地图，将地图数据可视化或输出到指定格式
map.render()

