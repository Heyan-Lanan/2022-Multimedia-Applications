import cv2 as cv
from matplotlib import pyplot as plt

# 参数0表示以灰度图像读入该图片，也就是说在读取的同时就进行了处理
# test.jpg, flower.jpg, cat.jpg
img = cv.imread('test2.jpg', 0)
# img.ravel()指最终的直方图将对数据集进行统计，256是统计的区间分布，[0,256]是显示的区间
plt.hist(img.ravel(), 256, [0, 256])
plt.show()
