import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



img = cv.imread('OPENCV/images/dog.jpg')

resiged_image = rescaleFrame(img, scale=0.2)

cv.imshow("Dog", resiged_image)
cv.imshow("DOG", img)



# Rescaling of Video  
# vid = cv.VideoCapture('OPENCV/video/dog.mp4') # uses video file

# while True:
#     isTrue, frame = vid.read(0)
    
#     frame_resized = rescaleFrame(frame, scale=0.2)
    
#     cv.imshow('Video', frame)
#     cv.imshow("Video Resized", frame_resized)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
    

cv.waitKey(0)