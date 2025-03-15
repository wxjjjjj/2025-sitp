# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:52:55 2025

@author: HP
"""

"""
请用pydicom库加载CT图像数据，并显示图像。    
"""


import pydicom
import matplotlib.pyplot as plt

# 读取dicom文件
ds = pydicom.dcmread(r"D:\BaiduNetdiskDownload\17F\剩余14位两次定位CT患者（17F）\20230205\20230205_1\CT.20230205_1.Image 85.dcm")

# 显示图像
plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
plt.show()