import cv2 as cv
import numpy as np

#极坐标变换
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/circle.png",cv.IMREAD_ANYCOLOR)
#设置参数，实现线性极坐标变换,(251,249)表示极坐标变换的中心,225表示极坐标变换的最大距离，cv.INTER_LINEAR表示线性插值算法
dst_linear = cv.linearPolar(image,(262,250),250,cv.INTER_LINEAR)
#设置参数，实现极坐标变换,M表示极坐标变换的系数
M1 = 20
M2 = 50
M3 = 90
#笛卡尔坐标向极坐标转换
dst_log1 = cv.logPolar(image,(262,250),M1,cv.WARP_FILL_OUTLIERS)
dst_log2 = cv.logPolar(image,(262,250),M2,cv.WARP_FILL_OUTLIERS)
dst_log3 = cv.logPolar(image,(262,250),M3,cv.WARP_FILL_OUTLIERS)

#显示图像
cv.imshow("image", image)
cv.imshow("dst_linear",dst_linear)
cv.imshow("dst_log1",dst_log1)
cv.imshow("dst_log2",dst_log2)
cv.imshow("dst_log3",dst_log3)
cv.waitKey()
cv.destroyAllWindows()
