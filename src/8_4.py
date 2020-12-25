import cv2 as cv
import numpy as np

#形态学开运算：先腐蚀，再膨胀
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/camel.png")
k = np.ones((10,10),np.uint8)
#也可以用erode和dilate来实现开运算,
#开运算可以消除亮度较高的细小区域，在纤细点处分离物体，较大物体可以在不明显改变面积情况下平滑其边界
openimg = cv.morphologyEx(image, cv.MORPH_OPEN, k)

cv.imshow("original image",image)
cv.imshow("openimg",openimg)
cv.waitKey()
cv.destroyAllWindows()

#形态学闭运算：先膨胀，再腐蚀
#也可以用erode和dilate来实现闭运算
#闭运算可以填充白色物体内细小黑色空洞的区域，连接临近物体等
closeimg = cv.morphologyEx(image, cv.MORPH_CLOSE, k)

cv.imshow("original image",image)
cv.imshow("closeimg",closeimg)
cv.waitKey()
cv.destroyAllWindows()