import cv2 as cv
faceDetector = cv.CascadeClassifier('ha_faceclas.xml')
img = cv.VideoCapture(0)
while img.isOpened():
    rect, frame = img.read()
    gray_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(gray_image, scaleFactor = 1.1, minNeighbors = 3)
    for (x, y, w, h) in faces:
        cv.rectangle(frame, pt1 = (x, y), pt2 = (x+w, y+h), color =(0,225,255), thickness = 3)
    cv.imshow("window", frame)
    if cv.waitKey(1) & 0xFF == ord('e'):
        break
frame.release()
cv.destroyAllWindows()
        
    
    