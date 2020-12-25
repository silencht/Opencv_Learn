import cv2 as cv

#局部阈值处理
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/lena.png",0)
#maxValue=255，最大值。cv.ADAPTIVE_THRESH_MEAN_C自适应方法。cv.THRESH_BINARY阈值处理方式。blockSize=5，块的大小。常量c=3
admean = cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,5, 3)
adguass = cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,5, 3)

cv.imshow("image",image)
cv.imshow("admean",admean)#显示局部阈值处理——邻域权重相同方式处理图像
cv.imshow("adguass",adguass)#显示局部阈值处理——高斯方程方式处理图像
cv.waitKey()
cv.destroyAllWindows()