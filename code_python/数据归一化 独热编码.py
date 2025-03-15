# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 13:31:54 2025

@author: HP
"""

import pandas as pd #pandas 是一个强大的数据分析库，用于处理表格数据
# import matplotlib.pyplot as plt #一个用于绘图的库，pyplot 是其子模块，用于绘制直方图、折线图等
# from scipy.stats import skew, kurtosis # 从 scipy.stats 模块中导入两个统计函数：skew 和 kurtosis。这两个函数分别用于计算数据的 偏度（Skewness） 和 峰度（Kurtosis），它们是描述数据分布形状的重要统计量
from sklearn.preprocessing import MinMaxScaler# ，StandardScaler 是标准化需要的库


#df = pd.read_csv(r"C:\Users\HP\Desktop\预测肿瘤体积变化率（输入特征）.csv", header=None)
#print(df.head())  # 打印前几行数据，检查数据结构

# 设置matplotlib支持中文，这样表格就不会出现方块or乱码的情况
# plt.rcParams['font.sans-serif'] = ['SimSun']  # Windows系统使用'SimSun'-宋体
# plt.rcParams['axes.unicode_minus'] = False    # 正确显示负号，Matplotlib 会使用字体中的普通字符（如 ASCII 中的 -）来渲染负号，而不是 Unicode 字符。这可以避免负号显示为乱码或方块的问题。

# 手动指定列名，csv中没弄列名
column_names = ["病案号", "分次剂量", "总次数","总剂量","第一次定位的GTV体积","两次定位的时间间隔","病理"]  # 根据你的数据结构调整列名
df = pd.read_csv(r"C:\Users\HP\Desktop\预测肿瘤体积变化率（输入特征）.csv", header=None, names=column_names)
# print(df.head())  # 打印前几行数据，检查数据结构--检查过了 设置的列名是正确的

# 对数值特征进行标准化
#scaler = StandardScaler()
#df[['第一次定位的GTV体积', '分次剂量', '总剂量', '两次定位的时间间隔']] = scaler.fit_transform(df[['第一次定位的GTV体积', '分次剂量', '总剂量', '两次定位的时间间隔']])
#print(df.head())  # 打印前几行数据

# 使用 MinMaxScaler 进行归一化--适用于数据分布不均匀的情况,不假设数据分布情况
scaler = MinMaxScaler()
df[['第一次定位的GTV体积', '分次剂量', '总剂量', '两次定位的时间间隔']] = scaler.fit_transform(df[['第一次定位的GTV体积', '分次剂量', '总剂量', '两次定位的时间间隔']])
# print("归一化后的数据：")
# print(df.head())
# 分类变量独热编码
df = pd.get_dummies(df, columns=['病理'])
# 调整显示设置
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 15)

# print(df.head())  # 打印前几行数据

# 绘制直方图
#plt.hist(df["第一次定位的GTV体积"], bins=20, edgecolor='black', density=True)
#plt.title("第一次定位的GTV体积")
#plt.xlabel("第一次定位的GTV体积")
#plt.ylabel("频率")
#plt.grid(axis='y', linestyle='--', alpha=0.7)
#plt.show()

# 计算偏度和峰度
#print("第一次定位的GTV体积偏度:", skew(df["第一次定位的GTV体积"]))
#print("第一次定位的GTV体积峰度:", kurtosis(df["第一次定位的GTV体积"]))