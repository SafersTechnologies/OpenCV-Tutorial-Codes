import cv2 as cv
vid = cv.VideoCapture('videos/drunken_master.3gp')
while True:
    isTrue, frame = vid.read()
    cv.imshow('Videoshow', frame)
    if cv.waitKey(30) & 0xFF == ord ('e'):
        break
vid.release()
cv.destroyAllWindows
    