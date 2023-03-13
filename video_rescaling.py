import cv2 as cv
def rescaleFrame(frame, scale=0.95):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
vid = cv.VideoCapture('videos/drunken_master.3gp')
while True:
    isTrue, frame = vid.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow ('Video', frame)
    cv.imshow ('resized Video', frame_resized)
    if cv.waitKey(100) & 0xFF == ord ('e'):
        break
vid.release()
cv.destroyAllWindows()