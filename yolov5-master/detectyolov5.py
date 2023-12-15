from pathlib import Path


import torch
from models.common import DetectMultiBackend
from utils.dataloaders import LoadImages
from utils.general import (LOGGER, check_img_size,
                           cv2, non_max_suppression, Profile, scale_boxes)
from utils.plots import Annotator, colors
from utils.torch_utils import select_device

weights = "F:\\FINAL PROJECT\\Project2\\UI\\sit up\\weights\\best.pt"
data = "C:\\Users\\66645\\Downloads\\sit up.yaml"
device = 'cpu'
source = "F:\\FINAL PROJECT\\Project2\\UI\\Cara-Melakukan-Sit-Up-yang-Efektif-bagi-Pemula.jpg"
imgsz = (416, 416)
hide_labels = False
hide_conf = False
max_det = 1000
agnostic_nms = False
classes = None
iou_thres = 0.45
conf_thres = 0.25

# Load model
device = select_device(device)
model = DetectMultiBackend(weights, device=device,
                           dnn=False, data=data, fp16=False)
stride, names, pt = model.stride, model.names, model.pt
imgsz = check_img_size(imgsz, s=stride)  # check image size

# Dataloader
dataset = LoadImages(source, img_size=imgsz, stride=stride, auto=pt)
bs = 1

# Run inference
model.warmup(imgsz=(1 if pt else bs, 3, *imgsz))  # warmup
seen, windows, dt = 0, [], (Profile(), Profile(), Profile())
for path, im, im0s, vid_cap, s in dataset:
    with dt[0]:
        im = torch.from_numpy(im).to(device)
        im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
        im /= 255  # 0 - 255 to 0.0 - 1.0
        if len(im.shape) == 3:
            im = im[None]  # expand for batch dim

    # Inference
    with dt[1]:
        pred = model(im)

    # NMS
    with dt[2]:
        pred = non_max_suppression(
            pred, conf_thres, iou_thres, classes, agnostic_nms, max_det=max_det)

    # Process predictions
    for i, det in enumerate(pred):  # per image
        seen += 1
        p, im0, frame = path, im0s.copy(), getattr(dataset, 'frame', 0)
        p = Path(p)  # to Path
        s += '%gx%g ' % im.shape[2:]  # print string
        gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
        annotator = Annotator(im0, line_width=3, example=str(names))
        if len(det):
            # Rescale boxes from img_size to im0 size
            det[:, :4] = scale_boxes(
                im.shape[2:], det[:, :4], im0.shape).round()

            # Print results
            for c in det[:, -1].unique():
                n = (det[:, -1] == c).sum()  # detections per class
                s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

            # Write results
            for *xyxy, conf, cls in reversed(det):
                c = int(cls)  # integer class
                label = None if hide_labels else (
                    names[c] if hide_conf else f'{names[c]} {conf:.2f}')
                annotator.box_label(xyxy, label, color=colors(c, True))

                print(label)

        # Stream results
        im0 = annotator.result()

        # Print time (inference-only)
        LOGGER.info(
            f"{s}{'' if len(det) else '(no detections), '}{dt[1].dt * 1E3:.1f}ms")

        # Print results
        t = tuple(x.t / seen * 1E3 for x in dt)  # speeds per image
        LOGGER.info(
            f'Speed: %.1fms pre-process, %.1fms inference, %.1fms NMS per image at shape {(1, 3, *imgsz)}' % t)

        cv2.imshow('results', im0)
        cv2.waitKey(0)
