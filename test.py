print("Hello World!")

"""
  我的注释
  我的注释
  我的注释
"""
money = 50
print("余额有:", money)
money_type = type(money)
print(money_type)
money_str = str(money)
print(money_str)
num = int("11")
print(type(num), num)
num_float = float(num)
print(num_float)

text_str = """
          《悯农》
    锄禾日当午，汗滴禾下土。
    谁知盘中餐，粒粒皆辛苦。
"""
print(text_str)

name = "Martin"
address = "中国"
tel = 18021420602
print("我的名字：%s，我的居住地址：%s，我的电话号码：%d" % (name, address, tel))
price = 99.99
print("%.2f" % price)
print(f"我的名字：{name}，我的居住地址：{address}，我的电话号码：{tel}，微信余额：{price}")
print(f"计算结果{(1 + 1) * 2 / (3 - ((1 + 1) * 1))}")
daily_growth_factor = 1.2

# print("输入姓名")
name = input("输入姓名:")
print(f"姓名：{name}")
print(f"姓名：{name}")
