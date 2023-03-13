import cv2 as cv
import numpy as np
img = cv.imread("Images/Seun.jpg")
def translate(img, x, y):
    TransMat = np.float32 ([[1, 0, x], [0, 1, y]])
    dimensions = [img.shape[0], img.shape[1]]
    return cv.warpAffine(img, TransMat, dimensions)
Translated_img = translate (img, -70, -50)
cv.imshow("Original Image", img)
cv.imshow("Translated Image", Translated_img)
cv.waitKey(0)
