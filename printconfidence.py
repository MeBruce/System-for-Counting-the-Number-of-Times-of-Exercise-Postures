import cv2
import torch
from torchvision.models.detection import yolo

# โหลดโมเดล YOLOv5
model = torch.load('C:\\Disk_F\\FINAL PROJECT\\Project2\\push up\\weights\\best.pt')

# สร้างตัวตรวจจับวัตถุ
detector = yolo.YOLOv5(model)

# เปิดกล้อง (ใช้ 0 สำหรับกล้องในเครื่อง, หรือระบุเส้นทางไปยังวิดีโอถ้าต้องการ)
cap = cv2.VideoCapture(0)

while True:
    # อ่านภาพจากกล้อง
    ret, frame = cap.read()

    # ใช้โมเดลตรวจจับวัตถุกับภาพ
    results = detector(frame)

    # ประมวลผลผลลัพธ์
    for result in results[0]:
        # ดึงค่าพิกัดกล่องรอบวัตถุ
        bbox = result['boxes']
    
        # ดึงค่าความมั่นใจในการตรวจจับวัตถุ
        confidence = result['scores']
    
        # ดึงค่าชื่อของวัตถุ
        label = result['labels']

        # แสดง Label และ Confidence บนคอนโซล
        print(f'Label: {label}, Confidence: {confidence:.2f}')

        # วาดกล่องรอบวัตถุที่ตรวจจับได้
        cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0, 255, 0), 2)

        # แสดง Label และ Confidence บน画面
        label_text = f'{label} ({confidence:.2f})'
        cv2.putText(frame, label_text, (int(bbox[0]), int(bbox[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # แสดงภาพที่ได้รับจากกล้อง
    cv2.imshow('YOLOv5 Object Detection', frame)

    # กด 'q' เพื่อออกจากการทำงาน
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ปิดกล้องและหน้าต่าง OpenCV
cap.release()
cv2.destroyAllWindows()
