import cv2
import numpy as np

# Load the pre-trained model
net = cv2.dnn.readNetFromTensorflow('pose_model.pb')

# Load the input image
image = cv2.imread('input_image.jpg')

# Prepare the input blob
blob = cv2.dnn.blobFromImage(image, 1.0, (368, 368), (127.5, 127.5, 127.5), swapRB=True, crop=False)

# Set the input blob for the network
net.setInput(blob)

# Forward pass through the network
output = net.forward()

# Get the detected keypoints
keypoints = output[0, :, :, :]

# Draw the keypoints on the image
for i in range(len(keypoints)):
    # Get the confidence score
    confidence = keypoints[i, 2]

    # Draw the keypoints only if the confidence is above a threshold
    if confidence > 0.5:
        # Get the x and y coordinates of the keypoint
        x = int(keypoints[i, 0] * image.shape[1])
        y = int(keypoints[i, 1] * image.shape[0])

        # Draw a circle at the keypoint position
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

# Display the image with keypoints
cv2.imshow('Human Pose Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
