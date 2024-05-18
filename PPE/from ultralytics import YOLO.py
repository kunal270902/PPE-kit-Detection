from ultralytics import YOLO
import cv2
#import cvzone
import math




model = YOLO('yolov8s_custom.pt')


img="55.mp4"
results = model.track(source=img, conf=0.3, iou=0.5, show=True)
