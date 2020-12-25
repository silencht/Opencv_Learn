import cv2 as cv
import numpy as np

#黑帽运算，原始图像减去闭运算结果
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/circle.png")
k = np.ones((10,10),np.uint8)
blackhat_img = cv.morphologyEx(image, cv.MORPH_BLACKHAT, k) #获得比原始图像边缘更加黑暗的边缘部分，或者获得图像内部的小孔

cv.imshow("original image",image)
cv.imshow("blackhat_img",blackhat_img)
cv.waitKey()
cv.destroyAllWindows()

#礼帽运算：原始图像减去开运算结果
tophat_img = cv.morphologyEx(image, cv.MORPH_TOPHAT, k) #获得图像的噪声信息，或者比原始图像边缘更亮的边缘部分
#也可以用erode和dilate来实现闭运算
cv.imshow("original image",image)
cv.imshow("tophat_img",tophat_img )
cv.waitKey()
cv.destroyAllWindows()