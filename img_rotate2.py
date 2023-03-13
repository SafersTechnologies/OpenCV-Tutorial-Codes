import cv2 as cv
img = cv.imread("Images/seun.jpg")
def rotate(img, angle, RotPt=None):
    (width, height) = img.shape[:2]
    if RotPt is None:
        rotPt = (width//2, height//2)
        rotMat = cv.getRotationMatrix2D(rotPt, angle, 1.0)
        dimensions = (width, height)
        return cv.warpAffine(img, rotMat, dimensions)
rotated_image = rotate(img, 150)
cv.imshow("Original Image", img)
cv.imshow("Rotated Image", rotated_image)
cv.waitKey(0)
        
    