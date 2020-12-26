import cv2 as cv
#Sobel算子
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/camel.png",0)
#设置参数 dx=1，dy=0，得到图像水平方向上的边缘信息
Sobelx = cv.Sobel(image,cv.CV_64F,1,0)
#对计算结果取绝对值
Sobelx = cv.convertScaleAbs(Sobelx)
#设置参数 dx=0，dy=1，得到图像垂直方向上的边缘信息
Sobely = cv.Sobel(image,cv.CV_64F,0,1)
#对计算结果取绝对值
Sobely = cv.convertScaleAbs(Sobely)
#设置参数 dx=1，dy=1，得到图像水平和垂直方向上的边缘信息
Sobelxy = cv.Sobel(image,cv.CV_64F,1,1)
#对计算结果取绝对值
Sobelxy = cv.convertScaleAbs(Sobelxy)
#利用加权函数对sobel算子水平和垂直方向上进行加权计算
Sobelxy_my = cv.addWeighted(Sobelx, 0.5, Sobely, 0.3,0)
#显示图像
cv.imshow("image",image)
cv.imshow("Sobelx",Sobelx)
cv.imshow("Sobely",Sobely)
cv.imshow("Sobelxy",Sobelxy)
cv.imshow("Sobelxy_my",Sobelxy_my)
cv.waitKey()
cv.destroyAllWindows()