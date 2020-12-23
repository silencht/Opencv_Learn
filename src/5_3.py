import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/flower.jpg",0) #读取一幅灰度图像

imageMax = np.max(image) #计算image的最大值
imageMin = np.min(image) #计算image的最小值
#确定输出最大灰度级与最小灰度级min_l = 0
min_l = 0
max_l = 255
#计算m、n的值
m = float(max_l-min_l)/(imageMax-imageMin)
n = min_l -imageMin *m
image1 = m * image + n
#矩阵的线性变换
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