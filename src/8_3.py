import cv2 as cv
import numpy as np

#形态学梯度运算
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/camel.png")
k1 = np.ones((2,2),np.uint8)
k2 = np.ones((5,5),np.uint8)
r1 = cv.morphologyEx(image, cv.MORPH_GRADIENT, k1) #实现图像的梯度运算
r2 = cv.morphologyEx(image, cv.MORPH_GRADIENT, k2)
cv.imshow("original image",image)
cv.imshow("r1",r1)
cv.imshow("r2",r2)
cv.waitKey()
cv.destroyAllWindows()