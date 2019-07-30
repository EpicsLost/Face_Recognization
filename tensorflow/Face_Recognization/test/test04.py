import cv2
import numpy as np

img = cv2.imread('1.jpg', 0)

# 先进行高斯滤波降噪。
img = cv2.GaussianBlur(img, (3, 3), 0)

# 在进行抠取轮廓，其中apertureSize默认为3。
canny = cv2.Canny(img, 200, 50)

cv2.imshow('canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
