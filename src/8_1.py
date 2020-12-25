import cv2 as cv
import numpy as np

#腐蚀
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/camel.png")
k = np.ones((3,3),np.uint8)
img = cv.erode(image, k, iterations=3) #腐蚀操作，迭代3次
cv.imshow("erode",img)
cv.waitKey()
cv.destroyAllWindows()