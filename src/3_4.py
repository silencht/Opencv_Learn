import cv2 as cv
import numpy as np
result_image1 = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/result.png")
cv.imshow("result_image1",result_image1)
result_image2 = np.zeros(result_image1.shape,dtype=np.uint8)#构造掩模图像
result_image2[100:400, 100:400] = 255
result_image_and = cv.bitwise_and(result_image1,result_image2)#进行按位与，取出掩模内的图像
result_image_or = cv.bitwise_or(result_image1,result_image2)#进行按位或，掩模内的图像变白
result_image_not = cv.bitwise_not(result_image1)#进行按位非，像素位均反转
cv.imshow("result_image_and",result_image_and)
cv.imshow("result_image_or",result_image_or)
cv.imshow("result_image_not",result_image_not)
cv.waitKey()
cv.destroyAllWindows()