import cv2
import torch
from PIL import Image

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt',  device='cpu')  # local model

# Initialize the camera (adjust the camera index as needed)
camera = cv2.VideoCapture(0)  # 0 for default camera

while True:
    # Capture a frame from the camera
    ret, frame = camera.read()
    
    # Convert the frame from BGR to RGB
    # im = frame[..., ::-1]
    im = frame
    
    # Inference
    results = model(im, size=640)
    
    # Get the annotated frame with bounding boxes
    annotated_frame = results.render()[0]
    a = results.pandas().xyxy[0]
    print(a["name"])
    
    
    # Display the annotated frame
    cv2.imshow('YOLOv5 Real-Time Object Detection', annotated_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close OpenCV windows
camera.release()
cv2.destroyAllWindows()
