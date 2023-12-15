import torch
from torchvision.models.detection import YOLOv5
from torchvision.ops import nms

# โหลดโมเดล YOLOv5
model = torch.load('F:\\FINAL PROJECT\\Project2\\UI\\sit up\\weights\\best.pt')

# สร้างตัวตรวจจับวัตถุ
detector = YOLOv5(model)

# โหลดภาพที่ต้องการตรวจจับ
image = 'F:\\FINAL PROJECT\\Project2\\UI\\sit up.jpg'

# ใช้โมเดลตรวจจับวัตถุกับภาพ
results = detector(image)

# ประมวลผลผลลัพธ์
for result in results:
    # ดำเนินการต่อไป...

    # กรองผลลัพธ์ด้วย non-maximum suppression
    boxes = result['boxes']
    scores = result['scores']
    labels = result['labels']
    
    keep = nms(boxes, scores, iou_threshold=0.5)
    
    filtered_boxes = boxes[keep]
    filtered_scores = scores[keep]
    filtered_labels = labels[keep]
    
    # ดำเนินการต่อไป...

#F:\\FINAL PROJECT\\Project2\\UI\\sit up\\weights\\best.pt
#F:\\FINAL PROJECT\\Project2\\UI\\sit up.jpg