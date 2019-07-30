import cv2

img = cv2.imread("0.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

sobel_x = cv2.Sobel(gray, cv2.CV_8U, 1, 0)
sobel_y = cv2.Sobel(gray, cv2.CV_8U, 0, 1)
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 1)

scharr_x = cv2.Scharr(gray, cv2.CV_8U, 1, 0)
scharr_y = cv2.Scharr(gray, cv2.CV_8U, 0, 1)

cv2.imshow("src", img)
cv2.imshow("Sobel_x", sobel_x)
cv2.imshow("Sobel_y", sobel_y)
cv2.imshow("Sobel", sobel)
cv2.imshow("Scharr_x", scharr_x)
cv2.imshow("Scharr_y", scharr_y)

cv2.waitKey(0)
