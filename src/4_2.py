import cv2 as cv
import numpy as np

#对矩阵进行重映射操作
img = np.random.randint(0,256,size=[6,6],dtype=np.uint8)
w ,h = img.shape #获取图像大小信息，shape[0]表示垂直尺寸，[1]代表水平尺寸
x = np.zeros((w,h),np.float32)
y = np.zeros((w,h),np.float32)
for i in range(w):
    for j in range(h):
        x.itemset((i,j),j)# x--W,y--H,所以x代表列，y代表行
        y.itemset((i,j),i)
rst = cv.remap(img,x,y,cv.INTER_LINEAR)#将矩阵重映射(这里为复制)至一个新的矩阵
print("image=\n",img)
print("rst=\n",rst)

#利用重映射复制图像操作
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/lena.png")
w ,h = image.shape[:2] #获取图像大小信息
print(w,h)
x = np.zeros((w,h),np.float32)
y = np.zeros((w,h),np.float32)
for i in range(w):
    for j in range(h):
        x.itemset((i,j),j)# x--W,y--H,所以x代表列，y代表行
        y.itemset((i,j),i)
rst = cv.remap(image,x,y,cv.INTER_LINEAR)#将图像重映射(这里为复制)至一个新的图像
cv.imshow("image",image)
cv.imshow("rst",rst)
cv.waitKey()
cv.destroyAllWindows()

#利用重映射对图像进行x轴翻转
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/lena.png")
w ,h = image.shape[:2] #获取图像大小信息
x = np.zeros((w,h),np.float32)
y = np.zeros((w,h),np.float32)
for i in range(w):
    for j in range(h):
        x.itemset((i,j),j)# x--W,y--H,所以x代表列，y代表行
        y.itemset((i,j),w-1-i)#绕x轴翻转，实际上是映射过程中x坐标轴的值不变，y坐标轴的值以x轴为对称轴进行交换
rst = cv.remap(image,x,y,cv.INTER_LINEAR)#将图像重映射(这里为绕X轴翻转)至一个新的图像
cv.imshow("image",image)
cv.imshow("rst",rst)
cv.waitKey()
cv.destroyAllWindows()

#利用重映射对图像进行y轴翻转
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/lena.png")
w ,h = image.shape[:2] #获取图像大小信息
x = np.zeros((w,h),np.float32)
y = np.zeros((w,h),np.float32)
for i in range(w):
    for j in range(h):
        x.itemset((i,j),h-1-j)# x--W,y--H,所以x代表列，y代表行
        y.itemset((i,j),i)#绕y轴翻转，实际上是映射过程中y坐标轴的值不变，x坐标轴的值以y轴为对称轴进行交换
rst = cv.remap(image,x,y,cv.INTER_LINEAR)#将图像重映射(这里为绕y轴翻转)至一个新的图像
cv.imshow("image",image)
cv.imshow("rst",rst)
cv.waitKey()
cv.destroyAllWindows()

#利用重映射对图像进行X/Y轴翻转
image = cv.imread("C:/Users/silencht/Desktop/Opencv_Learn/img/lena.png")
w ,h = image.shape[:2] #获取图像大小信息
x = np.zeros((w,h),np.float32)
y = np.zeros((w,h),np.float32)
for i in range(w):
    for j in range(h):
        x.itemset((i,j),h-1-j)# x--W,y--H,所以x代表列，y代表行
        y.itemset((i,j),w-1-i)#绕x/y轴翻转
rst = cv.remap(image,x,y,cv.INTER_LINEAR)#将图像重映射(这里为绕x/y轴翻转)至一个新的图像
cv.imshow("image",image)
cv.imshow("rst",rst)
cv.waitKey()
cv.destroyAllWindows()