import cv2 as cv
import matplotlib.pyplot as plt
#直方图统计
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/lena.png")
#直方图统计函数，[0]表示通道号，None表示不需要掩模图像，[256]表示灰度级分组BINS值，[0,256]表示像素值范围
hist = cv.calcHist([image],[0],None,[256],[0,255])
image_ravel = image.ravel() # 将图像转为一维数组

print(hist)
plt.plot(hist)#显示直方图
plt.show()

plt.hist(image_ravel,256) #绘制直方图
plt.show()

cv.imshow("image", image)
cv.waitKey()
cv.destroyAllWindows()
