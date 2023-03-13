import cv2 as cv
import numpy as np
blank = np.zeros((500, 500, 3), dtype ='uint8')
cv.putText(blank,  'Oluwaseun is my name', (50, 200), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 200, 225), 3)
cv.imshow("TEXT", blank)
cv.waitKey(0)