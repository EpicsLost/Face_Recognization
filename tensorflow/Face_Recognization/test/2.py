import cv2
import numpy as np
# img = cv2.imread("6.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imwrite("img2.jpg",img)

# cv2.waitKey(10000)
img = cv2.imread('1.jpg')
# 此处需注意，请参考后面的解释
res = np.uint8(np.clip((1.5 * img + 10), 0, 255))
#tmp = np.hstack((img, res))  # 两张图片横向合并（便于对比显示）

cv2.imshow('image', res)
cv2.waitKey(0)
