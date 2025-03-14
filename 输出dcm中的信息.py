# -*- coding: utf-8 -*-
import pydicom
 
path = r"D:\BaiduNetdiskDownload\17F\28位患者数据（17f）\28 patients\30 patients\20210281\20210281_1\RD.20210281.IMRT-3400.dcm"  # dicom文件路径
dicom = pydicom.dcmread(path, force=True)
# print(dicom)
# print("------------------------------------------------------------------------------------")
# print("------------------------------------------------------------------------------------")
# print(dicom.Modality) #Modality（影像模态）
# print(dicom.StudyDate) #拍摄时间
# print(dicom.PatientName) #Patient Name（患者姓名）
# print(dicom.PatientID) #Patient ID（患者ID）
# print(dicom.PatientSex) #Patient Sex（患者性别）                  （对勾）
# print(dicom.PatientBirthDate) #Patient Birth Date（患者出生日期） （对勾）
# print(dicom.SliceThickness) #Slice Thickness（切片厚度）
# print(dicom.Rows) #图像的宽
# print(dicom.Columns) #图像的长
# print(dicom.PixelSpacing) #Pixel Spacing（像素间距）
# print(dicom.ImageOrientationPatient) #Image Orientation (Patient)（图像定位（患者））
# print(dicom.SeriesDescription) #Series Description（系列描述）








