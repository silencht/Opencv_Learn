import numpy as np
import cv2 as cv
import math
import matplotlib.pyplot as plt

#计算图像灰度直方图
def calcGrayHist(image):
    #灰度图像矩阵的宽高
    rows,cols = image.shape
    #存储灰度直方图
    grayHist = np.zeros([256], np.uint32)
    for r in range(rows):
        for c in range(cols):
            grayHist[image[r][c]] += 1 #计算图片中每个像素灰度级的个数，储存到grayHist列表中
    return grayHist
#直方图均衡化
def equalHist(image):
    #灰度图像矩阵的宽高
    rows,cols = image.shape
    #计算灰度直方图
    grayHist = calcGrayHist(image)
    #计算累加灰度直方图
    zeroCumuMoment = np.zeros([256], np.uint32)
    for p in range(256):
        if p == 0:
            zeroCumuMoment[p] = grayHist[0]
        else:
            zeroCumuMoment[p] = zeroCumuMoment[p - 1] +grayHist[p]
    #根据直方图均衡化得到的输入灰度级和输出灰度级的映射
    outPut_q = np.zeros ([256], np.uint8)
    cofficient = 256.0 / (rows * cols) #系数
    for p in range(256):
        q = cofficient * float(zeroCumuMoment[p]) - 1 #当前累加灰度直方图的累加概率与灰度级的最大值256相乘得到新的灰度级
        if q >= 0:
            outPut_q[p] = math.floor(q) #向下取整
        else:
            outPut_q[p] = 0
    #得到直方图均衡化后的图像
    equalHistImage = np.zeros(image.shape, np.uint8)
    for r in range(rows):
        for c in range(cols):
            equalHistImage[r][c] = outPut_q[image[r][c]] #将像素原灰度级映射到均衡化后的灰度级，赋给新的图像空间
    return equalHistImage

#主函数
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/flower.jpg",0)
dst = equalHist(image) #直方图均衡化
#显示图像
cv.imshow("image", image) #显示原图像
cv.imshow("dst", dst) #显示均衡化图像
#显示原始图像直方图
plt.figure("原始直方图")
plt.hist(image.ravel (),256)
#显示均衡化后的图像直方图
plt.figure("均衡化直方图")
plt.hist(dst.ravel(), 256)
plt.show()
#直接用cv中自带的函数做均衡化
equ = cv.equalizeHist(image)
cv.imshow("equimage", equ)
cv.waitKey()
cv.destroyAllWindows()

#自适应直方图均衡化
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/flower.jpg",0)#创建CLAHE对象
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
#限制对比度的自适应阈值均衡化
dst = clahe.apply(image)
#显示图像
cv.imshow("image",image)
cv.imshow("clahe", dst)
plt.figure("原始直方图") #显示原始图像直方图
plt.hist(image.ravel(),256)
plt.figure("均衡化直方图") #显示均衡化后的图像直方图
plt.hist(dst.ravel(),256)
plt.show()
cv. waitKey()
cv.destroyAllWindows()
