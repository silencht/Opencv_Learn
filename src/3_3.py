import cv2 as cv
import numpy as np
#生成一个随机灰度图像和彩色图像
imagegray = np.random.randint(0,256,size=[256,256],dtype=np.uint8)
cv.imshow("imagegray",imagegray)
cv.waitKey()
cv.destroyAllWindows()
imagecolor = np.random.randint(0,256,size=[256,256,3],dtype=np.uint8)
cv.imshow("imagecolor",imagecolor)
cv.waitKey()
cv.destroyAllWindows()
