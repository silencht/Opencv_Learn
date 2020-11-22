import cv2 as cv

#读取图像
lena_image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/lena.png")
print(lena_image)
#创建窗口，显示图像
cv.namedWindow("image") #创建一个窗口
cv.imshow("image",lena_image)
cv.waitKey()
cv.destroyAllWindows()
#写入图像
cv.imwrite("C:/Users/silencht/Desktop/Opencv_Learn/img/result.png",lena_image)
#将图像bgr拆分
result_image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/result.png")
b, g, r = cv.split(result_image)
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)
cv.imshow("result_image",result_image)
cv.waitKey()
cv.destroyAllWindows()
#bgr合并图像
result_image_bgr = cv.merge([b, g, r])
cv.imshow("result_image_bgr",result_image_bgr)
cv.waitKey()
cv.destroyAllWindows()
#图像属性
print("result_image.shape",result_image.shape)
print("result_image.size",result_image.size)
print("result_image.dtype",result_image.dtype)