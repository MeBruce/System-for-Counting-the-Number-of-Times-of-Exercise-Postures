# Import PyTorch module
import torch
import cv2

# Download model from github
model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/best_squat.pt')

img = cv2.imread('37.png')
# img = cv2.resize(img, (1000, 650))

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Perform detection on image
result = model(img_rgb)
# Show image with bounding boxes
result.show()
print('result: ', result)
