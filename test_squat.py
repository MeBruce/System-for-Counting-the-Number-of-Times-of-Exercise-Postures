import tkinter as tk
from PIL import Image, ImageTk
import cv2
import torch

# Use GPU device='0' or force_reload=True Use CPU device='cpu'
model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/best_squat.pt',  force_reload=True, device='0') 
model.conf = 0.8
camera = cv2.VideoCapture(0) 

previous_object_name = None
count = 0
counting = False

def update_frame():
    ret, frame = camera.read()

    if frame is None:  
        print("Error: Couldn't read frame from camera")
        return
    
    rectangle_x = 100  
    rectangle_y = 10  
    rectangle_width = 200 
    rectangle_height = 450  
    
    cv2.rectangle(frame, (rectangle_x, rectangle_y), (rectangle_x + rectangle_width, rectangle_y + rectangle_height), (0, 255, 0), 2)
    
    frame_cropped = frame[rectangle_y:rectangle_y + rectangle_height, rectangle_x:rectangle_x + rectangle_width]
    
    frame_cropped = cv2.cvtColor(frame_cropped, cv2.COLOR_BGR2RGB) 

    results = model(frame_cropped, size=640)
    
    predictions = results.pandas().xyxy[0]

    global count, counting

    for index, row in predictions.iterrows():
        object_name = row['name'].strip()
        class_squat = row['class']
        print(class_squat, object_name)
        
        if counting:
            if object_name == 'squat up':
                count += 1
                counting = False
        elif object_name == 'squat down':
            counting = True


    # global count,counting

    # for index, row in predictions.iterrows():
    #     object_name = row['name']
    #     class_squat = row['class']
    #     print(class_squat, object_name)
        
    #     if object_name == "squat down":
    #         counting = True
    #     elif object_name == "squat up" and counting:
    #         count += 1
    #         counting = False



    # global previous_object_name, count

    # for index, row in predictions.iterrows():
    #     object_name = row['name']
    #     class_squat = row['class']
    #     print(class_squat, object_name)

    #     if previous_object_name == "squat down" and object_name == "squat up":
    #         count += 1
                
    #     previous_object_name = object_name
        


    # เมื่อพบว่าค่าการนับเกิน 99 ให้รีเซ็ตค่าการนับ
    if count > 99:
        reset_count()

    for index, row in predictions.iterrows():
        object_name = row['name']
        
        row['xmin'] += rectangle_x
        row['xmax'] += rectangle_x
        row['ymin'] += rectangle_y
        row['ymax'] += rectangle_y
        
        cv2.rectangle(frame, (int(row['xmin']), int(row['ymin'])), (int(row['xmax']), int(row['ymax'])), (255, 0, 0), 2)
        cv2.putText(frame, f"{row['name']}", (int(row['xmin']), int(row['ymin']) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 

    img = ImageTk.PhotoImage(image=Image.fromarray(frame))
    panel.img = img  
    panel.config(image=img)
    count_label.config(text=f'Count: {count}')  # แสดงจำนวนที่นับได้บน GUI
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
