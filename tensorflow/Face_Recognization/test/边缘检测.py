import cv2 as cv
def edge_image(image):
    blurred = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    cv.imshow("canny边缘", edge_output)
    dst = cv.bitwise_and(image, image, mask=edge_output)
    cv.imshow("color边缘", dst)

def edge_demo1(image):
    # 先将图像高斯模糊去噪
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    # 图像灰度化
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    # 图像边缘提取
    edge_output = cv.Canny(gray, 50, 150)
    cv.imshow("CannyEdge", edge_output)

    # 彩色边线
    # dst = cv.bitwise_and(image,gray,mask=edge_output)
    # cv.imshow("Color Edge",dst)

    return edge_output

src = cv.imread("1.jpg")
cv.imshow("原来", src)
edge_demo1(src)
#edge_image(src)
cv.waitKey(0)
cv.destroyAllWindows()