import tkinter as tk
from PIL import Image, ImageTk
import cv2
import torch

# Use GPU device='0' or force_reload=True Use CPU device='cpu'
model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/best_squat.pt',  force_reload=True, device='0') 
model.conf = 0.7
camera = cv2.VideoCapture(0) 

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

    results = model(frame, size=640)
    
    predictions = results.pandas().xyxy[0]
    
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

