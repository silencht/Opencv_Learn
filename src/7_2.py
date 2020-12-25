import cv2 as cv
import  numpy as np

#二值化阈值处理
image = np.random.randint(0,256,size=[6,6], dtype=np.uint8)#创建一个6*6的随机像素矩阵
th ,rst = cv.threshold(image,100,255,cv.THRESH_BINARY)#使用threshold函数进行二值化阈值处理,阈值设置为100,二值化后大像素灰度值为255
print("image=\n",image)
print("imagerst=\n",rst)

image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/lena.png",0)
ret ,dst = cv.threshold(image,127,255,cv.THRESH_BINARY)#阈值设置为127
cv.imshow("image",image)
cv.imshow("dst",dst)#显示二值化阈值处理后的图像
cv.waitKey()
cv.destroyAllWindows()

#反二值化阈值处理
ret_INV ,dst_INV = cv.threshold(image,127,255,cv.THRESH_BINARY_INV)#THRESH_BINARY_INV
cv.imshow("image",image)
cv.imshow("dst_INV",dst_INV)#显示反二值化阈值处理后的图像
cv.waitKey()
cv.destroyAllWindows()

#截断阈值处理
#当像素值大于设定的阈值时，该点像素值改为阈值；当像素值小于或等于设定的阈值时，该点像素值不发生改变
ret_TRUNC ,dst_TRUNC = cv.threshold(image,127,255,cv.THRESH_TRUNC)#THRESH_TRUNC
cv.imshow("image",image)
cv.imshow("dst_TRUNC",dst_TRUNC)#显示截断阈值处理后的图像
cv.waitKey()
cv.destroyAllWindows()

#超阈值零处理
#当像素值大于设定的阈值时，该点像素值改为0；当像素值小于或等于设定的阈值时，该点像素值不发生改变
ret_TOZERO_INV,dst_TOZERO_INV = cv.threshold(image,127,255,cv.THRESH_TOZERO_INV)#THRESH_TOZERO_INV
cv.imshow("image",image)
cv.imshow("dst_TOZERO_INV",dst_TOZERO_INV)
cv.waitKey()
cv.destroyAllWindows()

#低阈值零处理
#当像素值大于设定的阈值时，该点像素值不发生改变；当像素值小于或等于设定的阈值时，该点像素值改为0
ret_TOZERO,dst_TOZERO = cv.threshold(image,127,255,cv.THRESH_TOZERO)#THRESH_TOZERO
cv.imshow("image",image)
cv.imshow("dst_TOZERO",dst_TOZERO)
cv.waitKey()
cv.destroyAllWindows()