import cv2
from cv2 import imshow
from cv2 import threshold
from matplotlib import pyplot as py

img = cv2.imread("image.jpg")

print("Details :")
print("image size: ",img.size)
print("dimension: ",img.shape[0],"X",img.shape[1],"X",img.shape[2])

# Do thresholding with T=180
r, threshold = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
imshow("window",threshold)
cv2.waitKey(25000)

# convert to greyscale
img_new = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
imshow("window",img_new)
cv2.waitKey(25000)
