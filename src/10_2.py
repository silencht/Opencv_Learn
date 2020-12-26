import cv2 as cv

#Scharr算子
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/camel.png",0)
#设置参数 dx=1，dy=0，得到图像水平方向上的边缘信息
Scharrx = cv.Scharr(image,cv.CV_64F,1,0)
#对计算结果取绝对值
Scharrx = cv.convertScaleAbs(Scharrx)
#设置参数 dx=0，dy=1，得到图像垂直方向上的边缘信息
Scharry = cv.Scharr(image,cv.CV_64F,0,1)
#对计算结果取绝对值
Scharry = cv.convertScaleAbs(Scharry)

#通过设置cv2.Sobel函数的参数ksize=-1来计算图像水平和垂直方向上的边缘信息
Scharr_Sobel_x = cv.Sobel(image,cv.CV_64F,1, 0,-1)
Scharr_Sobel_x = cv.convertScaleAbs(Scharr_Sobel_x)
Scharry_Sobel_y = cv.Sobel(image,cv.CV_64F,0, 1,-1)
Scharr_Sobel_y = cv.convertScaleAbs(Scharry_Sobel_y)
#利用加权函数addWeighted水平和垂直方向上加权计算
Scharrxy_my=cv.addWeighted(Scharr_Sobel_x,0.5,Scharr_Sobel_y,0.3,0)

#显示图像
cv.imshow("image",image)
cv.imshow("Scharrx",Scharrx)
cv.imshow("Scharry",Scharry)
cv.imshow("Scharr_Sobel_x",Scharr_Sobel_x)
cv.imshow("Scharr_Sobel_y",Scharr_Sobel_y)
cv.imshow("Scharrxy_my",Scharrxy_my)
cv.waitKey()
cv.destroyAllWindows()