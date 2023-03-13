# import cv2 as cv
# import numpy as np
# blank = np.zeros((500, 400, 3), dtype ='uint8')
# cv.line(blank, (0,0), (170, 170), (0, 255, 0), thickness = 4)
# cv.imshow("Green Line", blank)
# cv.waitKey(0)

import cv2 as cv
import numpy as np
blank = np.zeros((500, 400, 3), dtype ='uint8')
cv.line(blank, (70, 70), (250, 280), (0, 255, 0), thickness = 4)
cv.imshow("Green Line", blank)
cv.waitKey(0)
