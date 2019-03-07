# -*- coding:utf-8 -*-
# /usr/bin/python

# 导入做图和数据处理的包
from mpl_toolkits.basemap import Basemap
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# 生成城市、房价、经度、纬度列表
citys = []
salesprice = []
lats = []
lons = []
for line in file("data.txt"):
    info = line.split()
    citys.append(info[0])
    salesprice.append(float(info[1]))
    lat = float(info[2][:-1])
    lats.append(lat)
    lon = float(info[3][:-1])
    lons.append(lon)

# 将图中的标签以仿宋体显示
mpl.rcParams[u'axes.unicode_minus'] = False
mpl.rcParams[u'font.sans-serif'] = u'SimHei'

# 绘制中国地图
size = 6500 * 1000  # 6500km
plt.figure(figsize=(10, 10), facecolor='w')
m = Basemap(width=size, height=size, projection='lcc', resolution='c', lat_0=35.5, lon_0=103.3)
m.drawcoastlines(linewidth=0.3, antialiased=False, color='#202020')  # 海岸线
m.drawrivers(linewidth=0.05, linestyle='-', color=(0.1, 0.1, 0.1), antialiased=False)  # 河流
m.drawcountries(linewidth=1, linestyle='-', antialiased=False)  # 国界
m.drawparallels(np.arange(0, 90, 10), labels=[True, True, False, False])  # 绘制平行线(纬线) [left,right,top,bottom]
m.drawmeridians(np.arange(0, 360, 15), labels=[False, False, False, True], linewidth=1, dashes=[2, 2])  # 绘制子午线
m.bluemarble()

# 将房价的大小以不同的圆圈显示
x, y = m(lons, lats)
max_price = max(salesprice)
size_factor = 500.0
y_offset = 150.0
rotation = 30
for i, j, k, city in zip(x, y, salesprice, citys):
    size = size_factor * k / max_price
    cs = m.scatter(i, j, s=size, marker='o', color='#FF5600')

# 绘制中国31个省市房价结构图
plt.tight_layout(4)
plt.title(u'各地区商品房平均销售价格(元/平方米)', fontsize=21)
plt.show()
