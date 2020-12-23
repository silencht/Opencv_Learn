import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
'''
所谓直方图正规化，就是通过一个灰度映像函数，将原灰度直方图改造成所希望的直方图。
所以，直方图修正的关键就是灰度映像函数。直方图正规化是用于产生处理后有特殊直方图的图像方法。
理想情况下，直方图均衡化实现了图像灰度的均衡分布，对提高图像对比度、提升图像 亮度具有明显的作用。
在实际应用中，有时并不需要图像的直方图具有整体的均匀分布，而希望直方图与规定要求的直方图一致，这就是直方图正规化。
它可以人为地改变原始图像直方图的形状，使其成为某个特定的形状，即增强特定灰度级分布范围内的图像。
'''
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/flower.jpg",0) #读取一幅灰度图像

imageMax = np.max(image) #计算image的最大值
imageMin = np.min(image) #计算image的最小值
#确定输出最大灰度级与最小灰度级min_l = 0
min_l = 0
max_l = 255
#计算m、n的值
m = float(max_l-min_l)/(imageMax-imageMin)
n = min_l -imageMin *m
image1 = m * image + n #矩阵的线性变换
image1 = image1.astype (np.uint8) #数据类型转换
#使用normalize函数实现正规化
image2 = cv.normalize(image,None, 255, 0, cv.NORM_MINMAX, cv.CV_8U)
#显示原始图像
cv.imshow("image", image)
plt.figure("原始直方图")
plt.hist(image.ravel(),256)
plt.figure("手动正规化后的直方图")
plt.hist(image1.ravel(),256)
plt.figure("函数正规化后的直方图")
plt.hist(image2.ravel(),256)
plt.show()
cv.waitKey()
cv.destroyAllWindows()