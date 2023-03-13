import cv2 as cv
captured_image = cv.VideoCapture(0)
while True:
    isTrue, frame = captured_image.read() 
    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord('r'):
        break
    
captured_image.release()
cv.destroyAllWindows()