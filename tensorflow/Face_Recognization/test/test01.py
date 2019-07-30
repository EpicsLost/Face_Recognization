from skimage import io, exposure
import matplotlib.pyplot as plt

img1 = io.imread('1.jpg',as_gray=True)
img2 = io.imread('0.jpg',as_gray=True)
#img = color.rgb2gray(img)
img1= exposure.adjust_gamma(img1, 0.7)
img2= exposure.adjust_gamma(img2, 0.8)
io.imshow(img1)
io.imshow(img2)
io.show()