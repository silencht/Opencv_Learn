import numpy as np
import cv2 as cv

image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/lena.png")
image_media = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/median.png")
image_bilateral = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/camel.png")

#高斯滤波
gauss = cv.GaussianBlur(image_bilateral,(5,5),0,0)#定义卷积核为5*5，采用自动计算权重的方式实现高斯滤波

#均值滤波
means5 = cv.blur(image,(5,5)) #定义卷积核为5*5，实现均值滤波
means10 = cv.blur(image,(10,10)) #定义卷积核为10*10，实现均值滤波
means20 = cv.blur(image,(20,20)) #定义卷积核为20*20，实现均值滤波

#方框滤波
box5_0 = cv.boxFilter(image,-1,(5,5),normalize=0) #定义卷积和为5*5, normalize=0不进行归一化
box2_0 = cv.boxFilter(image,-1,(2,2),normalize=0)#定义卷积和为2*2, normalize=0不进行归一化
box5_1 = cv.boxFilter(image,-1,(5,5),normalize=1) #定义卷积和为5*5, normalize=1进行归一化
box2_1 = cv.boxFilter(image,-1,(2,2),normalize=1)#定义卷积和为2*2, normalize=1进行归一化

#中值滤波
median = cv.medianBlur(image_media, 7)

#双边滤波
bilateral = cv.bilateralFilter(image_bilateral, 55, 100, 100)

#2d卷积核的实现
k = np.ones((9,9), np.float32)*2/81 #设置9*9的卷积核
out = cv.filter2D(image, -1, k)

#显示滤波后的图像
cv.imshow("image_bilateral", image_bilateral)
cv.imshow("gauss",gauss)
cv.imshow("bilateral", bilateral)
cv.waitKey(),cv.destroyAllWindows()

cv.imshow("image", image)
cv.imshow("means5",means5)
cv.waitKey()
cv.imshow("means10",means10)
cv.waitKey()
cv.imshow("means20",means20)
cv.waitKey(),cv.destroyAllWindows()

cv.imshow("image", image)
cv.imshow("box5_0", box5_0)
cv.waitKey()
cv.imshow("box2_0", box2_0)
cv.waitKey()
cv.imshow("box5_1", box5_1)
cv.waitKey()
cv.imshow("box2_1", box2_1)
cv.waitKey(),cv.destroyAllWindows()

cv.imshow("image_media", image_media)
cv.imshow("median", median)
cv.waitKey(),cv.destroyAllWindows()

cv.imshow("image", image)
cv.imshow("out", out)
cv.waitKey(),cv.destroyAllWindows()
