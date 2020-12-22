import cv2 as cv
import numpy as np

#投影变换
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/lena.png")
h ,w = image.shape[:2] #获取图像大小信息,shape[0]表示垂直尺寸，[1]代表水平尺寸
print(h,w)
#原图像需要变换的四个像素点
src = np.array([[0,0],[w-1,0],[0,h-1],[w-1,h-1]],np.float32)
#投影变换的4个像素点
dst = np.array([[5,5],[w/2,5],[250,h-1500],[w-500,h-1000]],np.float32)

M = cv.getPerspectiveTransform(src,dst)#计算出投影变换矩阵#进行投影变换
image1 = cv.warpPerspective(image,M, (w, h), borderValue=125)#对图像进行投影变换操作
#显示图像
cv.imshow("image", image)
cv.imshow("imagel",image1)
cv.waitKey()
cv.destroyAllWindows()
