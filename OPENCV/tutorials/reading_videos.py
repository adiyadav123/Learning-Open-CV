import cv2 as cv

vid = cv.VideoCapture(0) # uses webcam
# vid = cv.VideoCapture('OPENCV/video/dog.mp4') # uses video file

while True:
    isTrue, frame = vid.read()
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    

vid.release()
cv.destroyAllWindows()