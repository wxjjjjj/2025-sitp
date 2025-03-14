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
ds = pydicom.dcmread(r"D:\BaiduNetdiskDownload\17F\28位患者数据（17f）\28 patients\30 patients\20210281\20210281_1\CT.20210281.Image 1.dcm")

# 显示图像
plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
plt.show()