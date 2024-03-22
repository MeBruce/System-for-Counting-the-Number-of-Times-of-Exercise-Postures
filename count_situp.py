import cv2
import torch
from PIL import Image
import pandas as pd
import numpy as np

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/best_situp.pt',  device='cpu')  # Use GPU=0
model.conf = 0.7
# Initialize the camera (adjust the camera index as needed)
camera = cv2.VideoCapture(0)  # 0 for default camera

# Initialize variables for counting objects
previous_object_name = None
count = 0
sit_down_detected = False

def plot_counter(annotated_frame, count):
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 50)
    fontScale = 1
    color = (0, 255, 0) 
    thickness = 2

    # Create a copy of the annotated frame
    frame_with_text = annotated_frame.copy()
    
    # Add count text to the frame
    cv2.putText(frame_with_text, f'Count: {count}', org, font, fontScale, color, thickness)
    
    return frame_with_text

while True:
    # Capture a frame from the camera
    ret, frame = camera.read()
    
    # Convert the frame from BGR to RGB
    im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    
    # Inference
    results = model(im, size=640)
    
    # Get the object predictions
    predictions = results.pandas().xyxy[0]
    
    # Loop through the predictions and count object occurrences
    for index, row in predictions.iterrows():
        object_name = row['name']
        
        # Check if the object has changed from "sit down" to "sit up"
        if previous_object_name == "sit down" and object_name == "sit up":
            sit_down_detected = False
            count += 1
        elif previous_object_name == "sit up" and object_name == "sit down":
            sit_down_detected = True
        
        previous_object_name = object_name
    
    # Display the count
    print(f"Count: {count}")
    
    # Get the annotated frame with bounding boxes
    annotated_frame = results.render()[0]

    # Call the function to add count to the frame
    frame_with_text = plot_counter(annotated_frame, count)

    # Display the annotated frame
    cv2.imshow('count sit up', frame_with_text)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close OpenCV windows
camera.release()
cv2.destroyAllWindows()
