# import cv2
# import torch
# from PIL import Image
# import pandas as pd

# # Use GPU device='0' or force_reload=True Use CPU device='cpu'
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/best_situp.pt', device='cpu', force_reload=True) 
# model.conf = 0.7
# # Initialize the camera (adjust the camera index as needed)
# camera = cv2.VideoCapture(0)  # 0 for default camera

# # Initialize variables for counting objects
# previous_object_name = None
# count = 0
# sit_down_detected = False

# while True:
#     # Capture a frame from the camera
#     ret, frame = camera.read()
    
#     # Convert the frame from BGR to RGB
#     # im = frame[..., ::-1]
#     im = frame
    
#     # Inference
#     results = model(im, size=640)
    
#     # Get the object predictions
#     predictions = results.pandas().xyxy[0]
    
#     # Loop through the predictions and count object occurrences
#     for index, row in predictions.iterrows():
#         object_name = row['name']
        
#         # Check if the object has changed from "sit down" to "sit up"
#         if previous_object_name == "sit down" and object_name == "sit up":
#             sit_down_detected = False
#             count += 1
#         elif previous_object_name == "sit up" and object_name == "sit down":
#             sit_down_detected = True
        
#         previous_object_name = object_name
    
#     # Display the count
#     print(f"Count: {count}")
    
#     # Get the annotated frame with bounding boxes
#     annotated_frame = results.render()[0]
    
#     # Display the annotated frame
#     cv2.imshow('YOLOv5 Real-Time Object Detection', annotated_frame)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the camera and close OpenCV windows
# camera.release()
# cv2.destroyAllWindows()

import tkinter as tk
from PIL import Image, ImageTk
import cv2
import torch
import pandas as pd

# Use GPU device='0' or force_reload=True Use CPU device='cpu'
model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/best_squat.pt',  force_reload=True) 
model.conf = 0.7
camera = cv2.VideoCapture(0)  # 0 for default camera

previous_object_name = None
count = 0
sit_down_detected = False

def plot_counter(annotated_frame, count):
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 50)
    fontScale = 1
    color = (0, 255, 0) 
    thickness = 2

    frame_with_text = annotated_frame.copy()
    
    cv2.putText(frame_with_text, f'Count: {count}', org, font, fontScale, color, thickness)
    
    return frame_with_text

def update_frame():
    ret, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    
    im = Image.fromarray(frame)

    results = model(frame, size=640)
    
    predictions = results.pandas().xyxy[0]
    
    # Loop through the predictions and count object occurrences
    global previous_object_name, count, sit_down_detected
    for index, row in predictions.iterrows():
        object_name = row['name']
        
        if previous_object_name == "squat down" and object_name == "squat up":
            sit_down_detected = False
            count += 1
        elif previous_object_name == "squat up" and object_name == "squat down":
            sit_down_detected = True
        
        previous_object_name = object_name
        

    annotated_frame = results.render()[0]
    
    frame_with_text = plot_counter(annotated_frame, count)
    
    img = ImageTk.PhotoImage(image=Image.fromarray(annotated_frame))
    panel.img = img  
    
    panel.config(image=img)
    
    count_label.config(text=f'Count: {count}')
    
    panel.after(10, update_frame)

def reset_count():
    global count
    count = 0
    count_label.config(text=f'Count: {count}')
    

root = tk.Tk()
root.title("Count Squat")

panel = tk.Label(root)
panel.pack(padx=10, pady=10)

count_label = tk.Label(root, text=f'Count: {count}', font=("Helvetica", 30))
count_label.pack(padx=10, pady=10, anchor="w")  

reset_button = tk.Button(root, text="Reset",font=("Helvetica", 30), command=reset_count)
reset_button.place(x=450, y=505, width=185, height=60)


update_frame()

root.mainloop()

camera.release()

