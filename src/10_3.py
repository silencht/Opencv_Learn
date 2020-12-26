import cv2 as cv

#Canny算子
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/lena.png",0)
#设置不同的阈值信息对图像进行Canny边缘检测
edg1 = cv.Canny(image,30,100)
edg2 = cv.Canny(image,100,200)
edg3 = cv.Canny(image,200,255)
#显示图像
cv.imshow("image",image)
cv.imshow("edg1",edg1)
cv.imshow("edg2",edg2)
cv.imshow("edg3",edg3)
cv.waitKey()
cv.destroyAllWindows()