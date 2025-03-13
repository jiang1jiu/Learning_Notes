import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 打开并读取疫情数据文件
f = open("地图数据/疫情.txt", "r", encoding="utf_8")
date = f.read()

# 将JSON字符串解析为Python对象
data_dict = json.loads(date)
# 获取各省份的疫情数据
province_data_list = data_dict["areaTree"][0]["children"]

# 定义特殊省份的全称映射
special_provinces = {
    "北京": "市", "天津": "市", "上海": "市", "重庆": "市",
    "香港": "特别行政区", "澳门": "特别行政区",
    "新疆": "维吾尔自治区", "西藏": "自治区", "内蒙古": "自治区",
    "广西": "壮族自治区", "宁夏": "回族自治区"
}

# 初始化数据列表，用于绘图
data_list = []
# 遍历省份数据，构建绘图所需的数据格式
for province_data in province_data_list:
    province_name = province_data["name"]  # 获取省份名称
    province_confirm = province_data["total"]["confirm"]  # 获取确诊人数

    # 根据特殊省份的映射，更新省份名称
    if province_name in special_provinces:
        province_name += special_provinces[province_name]
    else:
        province_name += "省"

    # 将处理后的省份名称和确诊人数添加到数据列表中
    data_list.append((province_name, province_confirm))

# 创建地图对象
map = Map()
# 向地图对象中添加数据
map.add("国内疫情确诊人数", data_list, "china")
# 设置全局配置项，包括视觉映射配置
map.set_global_opts(
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


# 渲染全国疫情地图到HTML文件
map.render("全国疫情地图.html")


# 关闭文件流
f.close()
