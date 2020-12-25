import cv2 as cv
import numpy as np

#膨胀
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/lena.png")
k = np.ones((3,3),np.uint8)
img1 = cv.dilate(image, k, iterations=1) #膨胀操作，迭代1次
img2 = cv.dilate(image, k, iterations=2) #膨胀操作，迭代2次
img3 = cv.dilate(image, k, iterations=3) #膨胀操作，迭代3次
cv.imshow("dilate1",img1)
cv.imshow("dilate2",img2)
cv.imshow("dilate3",img3)
cv.waitKey()
cv.destroyAllWindows()