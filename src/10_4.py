import cv2 as cv
#拉普拉斯算子
image=cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/camel.png",0)#读取一幅灰度图
#使用拉普拉斯算子计算边缘信息
laplacian = cv.Laplacian(image,cv.CV_64F)
laplacian = cv.convertScaleAbs(laplacian)#对计算结果取绝对值
#显示图像
cv.imshow("image",image)
cv.imshow("laplacian",laplacian)
cv.waitKey()
cv.destroyAllWindows()
