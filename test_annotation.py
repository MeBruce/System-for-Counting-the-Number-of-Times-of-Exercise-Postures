import tkinter as tk
from PIL import Image, ImageTk
import cv2
import torch

# โหลดโมเดล YOLOv5 ที่ถูกฝึกอบรมเอง
model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/best_squat.pt', force_reload=True, device='0') 
model.conf = 0.7

# เปิดกล้อง
camera = cv2.VideoCapture(0) 

# กำหนดตัวแปรสำหรับการตรวจจับการกางตัวก่อนหน้า, จำนวนครั้งที่นับได้, และสถานะการกางตัว
previous_object_name = None
count = 0
sit_down_detected = False

# ฟังก์ชันสำหรับอัพเดตภาพจากกล้องและการตรวจจับการกางตัว
def update_frame():
    ret, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 

    results = model(frame, size=640)
    predictions = results.pandas().xyxy[0]
    print(predictions)
    # กำหนดตำแหน่งและขนาดของกรอบสี่เหลี่ยม
    rectangle_x = 100  # ตำแหน่ง x ของมุมบนซ้ายของกรอบสี่เหลี่ยม
    rectangle_y = 10  # ตำแหน่ง y ของมุมบนซ้ายของกรอบสี่เหลี่ยม
    rectangle_width = 200  # ความกว้างของกรอบสี่เหลี่ยม
    rectangle_height = 500  # ความสูงของกรอบสี่เหลี่ยม

    global previous_object_name, count, squat_up_detected

    # วนลูปผ่านการทำนายของโมเดลสำหรับวัตถุในภาพ
        # วนลูปผ่านการทำนายของโมเดลสำหรับวัตถุในภาพ
    for index, row in predictions.iterrows():
        # ดึงชื่อของวัตถุจากผลลัพธ์การทำนาย
        object_name = row['name']
        
        # ตรวจสอบว่าวัตถุอยู่ภายในกรอบสี่เหลี่ยมหรือไม่
        if rectangle_x < row['xmin'] < rectangle_x + rectangle_width and rectangle_y < row['ymin'] < rectangle_y + rectangle_height:
            # กรอบสี่เหลี่ยมที่กำหนด
            # ดำเนินการเมื่อตรวจพบวัตถุอยู่ในกรอบสี่เหลี่ยม
            # ในที่นี้คือตรวจสอบการกางตัวและนับ
            if object_name == "squat up":
                # หากพบการกางตัวขึ้น
                # ระบุว่ามีการกางตัวขึ้น
                squat_up_detected = True
            elif object_name == "squat down" and squat_up_detected:
                # หากพบการกางตัวลงหลังจากการกางตัวขึ้นแล้ว
                # เพิ่มจำนวนการนับได้
                count += 1
                # ระบุว่าไม่มีการกางตัวขึ้นอีก
                squat_up_detected = False

    # อัพเดตภาพที่มีการวาดกรอบสี่เหลี่ยม
    cv2.rectangle(frame, (rectangle_x, rectangle_y), (rectangle_x + rectangle_width, rectangle_y + rectangle_height), (0, 255, 0), 2)
    
    # แปลงสี BGR เป็น RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # แปลง array ของภาพเป็นรูปแบบที่รองรับได้กับ tkinter
    img = Image.fromarray(frame_rgb)
    img = ImageTk.PhotoImage(image=img)

    # แสดงภาพที่มีการวาดกรอบสี่เหลี่ยมแล้ว
    panel.img = img  
    panel.config(image=img)
    
    # อัพเดตจำนวนครั้งที่นับได้บนหน้าต่าง tkinter
    count_label.config(text=f'Count: {count}')
    
    # เรียกใช้ฟังก์ชันอัพเดตเฟรมอีกครั้งหลังจาก 10 มิลลิวินาที
    if ret:
        panel.after(10, update_frame)

# ฟังก์ชันสำหรับรีเซ็ตจำนวนครั้งที่นับได้
def reset_count():
    global count
    count = 0
    count_label.config(text=f'Count: {count}')

# สร้างหน้าต่าง tkinter
root = tk.Tk()
root.title("Count Squat")

# สร้างแผงเพื่อแสดงภาพ
panel = tk.Label(root)
panel.pack(padx=10, pady=10)

# สร้างป้ายกำกับสำหรับแสดงจำนวนครั้งที่นับได้
count_label = tk.Label(root, text=f'Count: {count}', font=("Helvetica", 30))
count_label.pack(padx=10, pady=10, anchor="w")  

# สร้างปุ่มสำหรับรีเซ็ตค่า
reset_button = tk.Button(root, text="Reset", font=("Helvetica", 30), command=reset_count)
reset_button.place(x=450, y=505, width=185, height=60)

# เริ่มต้นการอัพเดตภาพ
update_frame()

# เริ่มการทำงานของหน้าต่าง tkinter
root.mainloop()

# ปิดการเชื่อมต่อกล้องหลังจากทำงานเสร็จสิ้น
camera.release()
#yoyo