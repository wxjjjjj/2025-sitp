"""
Created on Sat Mar 15 12:40:01 2025

@author: HP
"""

import pandas as pd #pandas 是一个强大的数据分析库，用于处理表格数据
from sklearn.preprocessing import MinMaxScaler# ，StandardScaler 是标准化需要的库
from sklearn.model_selection import train_test_split #数据集、训练集划分库
from sklearn.linear_model import LinearRegression # 线性回归模型库
from sklearn.metrics import mean_squared_error, r2_score # 测试集预测 评估模型性能
import matplotlib.pyplot as plt #可视化 库

# 设置matplotlib支持中文，这样表格就不会出现方块or乱码的情况
plt.rcParams['font.sans-serif'] = ['SimSun']  # Windows系统使用'SimSun'-宋体
plt.rcParams['axes.unicode_minus'] = False    # 正确显示负号，Matplotlib 会使用字体中的普通字符（如 ASCII 中的 -）来渲染负号，而不是 Unicode 字符。这可以避免负号显示为乱码或方块的问题。

# 手动指定列名，csv中没弄列名
column_names = ["病案号", "分次剂量", "总次数","总剂量","第一次定位的GTV体积","两次定位的时间间隔","病理"]  # 根据你的数据结构调整列名
df = pd.read_csv(r"C:\Users\HP\Desktop\预测肿瘤体积变化率（输入特征）.csv", header=None, names=column_names)

# 使用 MinMaxScaler 进行归一化--适用于数据分布不均匀的情况,不假设数据分布情况
scaler = MinMaxScaler()
df[['第一次定位的GTV体积', '分次剂量', '总剂量', '两次定位的时间间隔']] = scaler.fit_transform(df[['第一次定位的GTV体积', '分次剂量', '总剂量', '两次定位的时间间隔']])

# 分类变量独热编码
df= pd.get_dummies(df, columns=['病理'])

# 读取包含目标变量的 CSV 文件
target_column_names = ["第二次定位的GTV体积","病案号" ]
target_df = pd.read_csv(r"C:\Users\HP\Desktop\第二次GTV体积（作为验证）.csv", header=None, names=target_column_names)

# 合并数据集
df = pd.merge(df, target_df, on="病案号")

# 提取特征
X = df[["分次剂量", "总次数", "总剂量", "第一次定位的GTV体积", "两次定位的时间间隔", "病理_AC", "病理_NSCLC","病理_SCC","病理_SCLC"]]  # 根据独热编码后的列名调整

# 提取目标变量（肿瘤体积变化率）
Y = df["第二次定位的GTV体积"]

#将数据集拆分为训练集和测试集
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# 训练模型
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# 预测
Y_pred = regressor.predict(X_test)

# 计算均方误差
mse = mean_squared_error(Y_test, Y_pred)
print(f"Mean Squared Error: {mse}")
# 计算均方根误差（RMSE）
rmse = mse ** 0.5  # 或者使用 numpy.sqrt(mse)
print(f"Root Mean Squared Error (RMSE): {rmse}")
# 计算 R^2 值
r2 = r2_score(Y_test, Y_pred)
print(f"R^2 Score: {r2}")

#图表可视化
plt.scatter(Y_test, Y_pred)
plt.xlabel("实际的第二次定位的GTV体积")
plt.ylabel("预测的第二次定位的GTV体积")
plt.title("预测结果与实际结果的对比")
plt.show()

