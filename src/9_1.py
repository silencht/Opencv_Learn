import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#分水岭算法

image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/coin.png")
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY) #将图像转为灰度图
#找出硬币的近似估计，对灰度图使用otsu阈值处理
ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
cv.imshow('1.thresh', thresh)
#对二值图像进行开运算，移除图像的噪声
kernel = np.ones((3,3), np.uint8) #设置开运算的卷积核
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)
cv.imshow('2.opening', opening)
#对开运算后的图像进行膨胀操作，得到确定的背景
sure_bg = cv.dilate(opening, kernel, iterations=3) #膨胀操作，迭代3次
cv.imshow('3.sure_bg', sure_bg)
#计算欧氏距离，并对距离图像进行阈值处理,得到确定前景(即确定的硬币区域)，离零像素（黑暗背景）越远，距离越大，越亮
dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
plt.figure("4.dist_transform")
plt.imshow(dist_transform)
plt.axis("off")
plt.show()
ret1, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
cv.imshow('5.sure_fg', sure_fg)
#找出不确定的未知区域
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg, sure_fg)
cv.imshow('6.unknown', unknown)
#用函数对区域加标签，输出结果是确认的前景为从 1 开始的正整数（此处存疑），在此之外的背景为 0,但是我们不想让背景为0，因为那意味着背景是未知区域的
#所以我们把结果整体 +1，使得前景标签为2，背景标签为 1 ，最后将未知区域的像素位置标签为 0
ret2, markers = cv.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0
#使用分水岭算法
markers = cv.watershed(image, markers)
#将边界标记为蓝色
image[markers == -1] = [255,0,0]

cv.imshow('7.watershed', image)

cv.waitKey()
cv.destroyAllWindows()
