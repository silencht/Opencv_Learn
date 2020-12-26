import cv2 as cv
import numpy as np
#图像的金字塔分割

#下采样，原始图像和各级下采样所得到的图像共同构成了高斯金字塔
img1 = cv.pyrDown(image)#第一次下采样
img2 = cv.pyrDown(img1)#第二次下采样
img3 = cv.pyrDown(img2)
cv.imshow("image",image)
cv.imshow("img1",img1)
cv.imshow("img2",img2)
cv.imshow("img3",img3)

print("image.shape",image.shape)
print("img1.shape",img1.shape)
print("img2.shape",img2.shape)
print("img3.shape",img3.shape)

cv.waitKey()
cv.destroyAllWindows()
#上采样
img1 = cv.pyrUp(image)#第一次上采样
img2 = cv.pyrUp(img1)#第二次上采样
img3 = cv.pyrUp(img2)
cv.imshow("image",image)
cv.imshow("img1",img1)
cv.imshow("img2",img2)
cv.imshow("img3",img3)
print("image.shape",image.shape)
print("img1.shape",img1.shape)
print("img2.shape",img2.shape)
print("img3.shape",img3.shape)

cv.waitKey()
cv.destroyAllWindows()
#利用pyrDown和pyrUp实现拉普拉斯金字塔，
#拉普拉斯金字塔的某一层图像是源图像减去先缩小再放大的图像（即先下采样后的图像再上采样）
#拉普拉斯金字塔记录了高斯金字塔每一级下采样后再上采样 与 下采样前的差异
img0 = image
img1 = cv.pyrDown(img0)#第一次下采样
img2 = cv.pyrDown(img1)#第二次下采样
img3 = cv.pyrDown(img2)#第三次下采样

img1_up = cv.pyrUp(img1)
img2_up = cv.pyrUp(img2)
img2_up = np.delete(img2_up,1159,0)
img3_up = cv.pyrUp(img3)
img3_up = np.delete(img3_up,271,1)

I0 = img0 - img1_up #第一层拉普拉斯金字塔
I1 = img1 - img2_up #第二层拉普拉斯金字塔
I2 = img2 - img3_up #第三层拉普拉斯金字塔

cv.imshow("I0",I0)
cv.imshow("I1",I1)
cv.imshow("I2",I2)
cv.waitKey()
cv.destroyAllWindows()

#通过高斯金字塔和拉普拉斯金字塔实现对图像的分割及复原
#恢复高精度图像
M0 = I0 + img1_up
M1 = I1 + img2_up
M2 = I2 + img3_up
cv.imshow("image",image)
cv.imshow("M0",M0)
cv.imshow("M1",M1)
cv.imshow("M2",M2)

cv.waitKey()
cv.destroyAllWindows()