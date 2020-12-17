import cv2 as cv
lena_imageBGR = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/lena.png")
cv.imshow("lena_imageBGR",lena_imageBGR)
lena_imageRGB = cv.cvtColor(lena_imageBGR,cv.COLOR_BGR2RGB) #BGR色彩空间转RGB色彩空间
cv.imshow("lena_imageRGB",lena_imageRGB)#该RGB色彩空间的图像蓝色相对于BGR色彩空间比较凸显
cv.waitKey()
cv.destroyAllWindows()