"""
要求：
    计算经过growth_days天增长后，股价达到了多少钱
    使用字符串格式化进行输出，如果是浮点数，要求小数点精度2位数
"""
name = "船只"   # 公司名称
stock_prick = 19.99   # 当前股价
stock_code = "030032"   # 股票代码
s_p_d_g_f = 1.2  # 股票每日增长系数，浮点数类型
growth_days = 7  #增长天数
money = 19.99 * 1.2 ** 7  # 七天之后的股价
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_prick}")
print("每日增长系数：%.1f，经过%d天的增长后，股价达到了 %.2f" % (s_p_d_g_f, growth_days,money))