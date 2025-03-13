import json
from pyecharts.charts import Map
from pyecharts.options import *
# 打开文件
f = open("地图数据/疫情.txt", "r", encoding="utf-8")
# 读取文件内容
data = f.read()
# 将json文件转换成python字典
data_dict = json.loads(data)
# 获取河南省的内容
hn_data_dict = data_dict["areaTree"][0]["children"][3]["children"]
# 初始化数据
data_list = []
# 遍历获取到的内容变成可用数据
for city_data in hn_data_dict:
    city_name = city_data["name"] + "市"  # 获取省内市的名字
    city_confirm = city_data["total"]["confirm"]  # 确诊人数
    data_list.append((city_name, city_confirm))
data_list.append(("济源市", 5))
map = Map()
map.add("河南省疫情分布", data_list, "河南")
# 设置全局配置项，包括视觉映射配置
map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 显示视觉映射
        is_piecewise=True,  # 使用分段视觉映射
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#99FF99"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#66FFFF"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#FF8800"},
            {"min": 1000, "max": 9999, "label": "1000-9999", "color": "#FF0000"},
            {"min": 10000,  "label": "10000+", "color": "#880000"}
        ]
    )
)


map.render("河南省疫情分布.html")
f.close()
