import numpy as np
import math
import cv2 as cv
from scipy import signal
#构建LoG算子
def createLoGKernel(sigma,kSize):
    # LoG算子的宽和高，且两者均为奇数
    winH, winW = kSize
    logKernel = np.zeros (kSize,np.float32)
    #方差
    sigmaSquare = pow(sigma,2.0)
    # LoG算子的中心
    centerH = (winH-1)/2
    centerW = (winW-1)/2
    for r in range(winH):
        for c in range (winW):
             norm2 = pow(r-centerH,2.0) + pow (c-centerW,2.0)
             logKernel[r][c]= 1.0/sigmaSquare * (norm2/sigmaSquare- 2)*math.exp(-norm2/(2* sigmaSquare))
    return logKernel
#LoG卷积，一般取_boundary = 'symm'
def LoG(image,sigma,kSize,_boundary='fill',_fillValue = 0):
    #构建LoG卷积核
    loGKernel = createLoGKernel(sigma,kSize)
    #图像与LoG卷积核卷积
    img_conv_log = signal.convolve2d(image,loGKernel,'same', boundary =_boundary)
    return img_conv_log
def edge_binary(img):
    edge = np.copy(img)
    edge[edge >= 0] = 0
    edge[edge < 0] = 255
    edge = edge.astype(np.uint8)
    return edge
#主函数
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/lena.png",0)
#显示原图
cv.imshow("image", image)
#LoG卷积
img1 = LoG(image,2,(7,7),'symm')
img2 = LoG(image,2,(11,11), 'symm')
img3 = LoG(image,2,(13,13), 'symm')
#边缘的二值化显示
L1 = edge_binary(img1)
L2 = edge_binary(img2)
L3 = edge_binary(img3)
#显示LoG边缘检测结果
cv.imshow("L1",L1)
cv.imshow("L2",L2)
cv.imshow("L3",L3)
cv.waitKey()
cv.destroyAllWindows()

