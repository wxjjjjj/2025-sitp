# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 11:17:02 2025

@author: HP
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 导入数据集
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['花萼-length', '花萼-width', '花瓣-length', '花瓣-width', 'class']
dataset = pd.read_csv(url, names=names)

# 提取花瓣数据
X = dataset["花瓣-length"].values.reshape(-1, 1)
Y = dataset["花瓣-width"].values.reshape(-1, 1)

# 拆分数据集
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# 训练模型
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# 可视化结果
plt.scatter(X_train, Y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='green')
plt.xlabel("length") #只有英文的才能在图表中显示 （之前的“花瓣长度”的中文就显示不了）
plt.ylabel("width")
plt.title("result")
plt.show()