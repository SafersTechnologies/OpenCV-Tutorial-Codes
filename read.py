import cv2 as cv
cam = cv.VideoCapture(0)
cv.namedWindow("Webcam Image")
img_counter = 0
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab")
        break
    cv.imshow("test", frame)
    k=cv.waitKey(1) & 0xFF == ord ('r')
    if k%256 == 27:
        print("Escape hit, closing app")
    
    elif k%256 ==32:
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv.imwrite(img_name, frame)
        print ("screenshot taken")
        img_counter+=1
    
cam.release()
cv.destroyAllWindows()