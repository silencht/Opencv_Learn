import cv2 as cv
import numpy as np

image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/lena.png")
h ,w = image.shape[:2] #获取图像大小信息
M = np.float32([[1,0,120],[0,1,-120]]) #构建平移转换矩阵
S = np.float32([[0.5,0,0],[0,0.3,0]]) #构建缩放转换矩阵
RET = cv.getRotationMatrix2D((w/3,h/3),45,1) #构建旋转转换矩阵，效果是以图像的宽高的1/3为中心点，顺时针旋转45°，缩小为原来的0.5

imageMove = cv.warpAffine(image,M,(w,h)) #进行仿射变换——平移
imageScale = cv.warpAffine(image,S,(w,h)) #进行仿射变换——缩放
imageRot = cv.warpAffine(image,RET,(w,h)) #进行仿射变换——旋转

cv.imshow("image",image)
cv.imshow("imageMove",imageMove)
cv.imshow("imageScale",imageScale)
cv.imshow("imageRot",imageRot)
cv.waitKey()
cv.destroyAllWindows()

