import cv2 as cv
lena_imageBGR = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/lena.png")

lena_imageRGB = cv.cvtColor(lena_imageBGR,cv.COLOR_BGR2RGB) #BGR色彩空间转RGB色彩空间
lena_imageGRAY = cv.cvtColor(lena_imageRGB,cv.COLOR_RGB2GRAY)#RGB色彩空间转GRAY色彩空间
lena_imageYCrCb = cv.cvtColor(lena_imageRGB,cv.COLOR_RGB2YCrCb)#RGB色彩空间转YCrCb色彩空间
lena_imageHSV = cv.cvtColor(lena_imageRGB,cv.COLOR_RGB2HSV)#RGB色彩空间转HSV色彩空间

cv.imshow("lena_imageBGR",lena_imageBGR)
cv.imshow("lena_imageRGB",lena_imageRGB)#该RGB色彩空间的图像蓝色相对于BGR色彩空间比较凸显
cv.imshow("lena_imageGRAY",lena_imageGRAY)
cv.imshow("lena_imageYCrCb",lena_imageYCrCb)#该空间有亮度信息，弥补了RGB空间没有亮度信息的遗憾
cv.imshow("lena_imageHSV",lena_imageHSV)

cv.waitKey()
cv.destroyAllWindows()
