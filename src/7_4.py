import cv2 as cv

#使用otsu阈值处理
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/lena.png",0)
t ,otsu = cv.threshold(image,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU) #使用otsu时必须把阈值设为0
cv.imshow("image",image)
cv.imshow("otsu",otsu)
print("otsu的阈值是：%s"%t) #输出阈值
cv.waitKey()
cv.destroyAllWindows()