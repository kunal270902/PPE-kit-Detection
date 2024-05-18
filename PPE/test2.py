from ultralytics import YOLO
import cv2
import math

class POS_System:
    def _init_(self):
        self.scanned_items = {"tomato": 1, "juice": 1, "chocolate": 1}  # Using manually typed dictionary to verify
        self.detected_items = {}

    """
    here you can integrate a product scanning device with system as you scan the product it should 
    append that product name to the scanned item dictionary
    """

    # def scan_item(self, item):
    #     self.scanned_items.append(item)
    def detect_item(self, item):
        if item in self.detected_items:
            self.detected_items[item] += 1
        else:
            self.detected_items[item] = 1

# Initialize supermarket POS system
pos_system = POS_System()

# Initialize empty list to store detected labels
detected_labels = []

# Load pre-trained YOLO model for object tracking
model = YOLO('yolov8n.pt')
classNames={
    0: '_background_',
    1: 'person',
    2: 'bicycle',
    3: 'car',
    4: 'motorcycle',
    5: 'airplane',
    6: 'bus',
    7: 'train',
    8: 'truck',
    9: 'boat',
    10: 'traffic light',
    11: 'fire hydrant',
    12: 'stop sign',
    13: 'parking meter',
    14: 'bench',
    15: 'bird',
    16: 'cat',
    17: 'dog',
    18: 'horse',
    19: 'sheep',
    20: 'cow',
    21: 'elephant',
    22: 'bear',
    23: 'zebra',
    24: 'giraffe',
    25: 'backpack',
    26: 'umbrella',
    27: 'handbag',
    28: 'tie',
    29: 'suitcase',
    30: 'frisbee',
    31: 'skis',
    32: 'snowboard',
    33: 'sports ball',
    34: 'kite',
    35: 'baseball bat',
    36: 'baseball glove',
    37: 'skateboard',
    38: 'surfboard',
    39: 'tennis racket',
    40: 'bottle',
    41: 'wine glass',
    42: 'cup',
    43: 'fork',
    44: 'knife',
    45: 'spoon',
    46: 'bowl',
    47: 'banana',
    48: 'apple',
    49: 'sandwich',
    50: 'orange',
    51: 'broccoli',
    52: 'carrot',
    53: 'hot dog',
    54: 'pizza',
    55: 'donut',
    56: 'cake',
    57: 'chair',
    58: 'couch',
    59: 'potted plant',
    60: 'bed',
    61: 'dining table',
    62: 'toilet',
    63: 'tv',
    64: 'laptop',
    65: 'mouse',
    66: 'remote',
    67: 'keyboard',
    68: 'cell phone',
    69: 'microwave',
    70: 'oven',
    71: 'toaster',
    72: 'sink',
    73: 'refrigerator',
    74: 'book',
    75: 'clock',
    76: 'vase',
    77: 'scissors',
    78: 'teddy bear',
    79: 'hair drier',
    80: 'toothbrush'
}

img="55.mp4"
# Run the tracker
results = model.track(source=img, conf=0.3, iou=0.5, show=True)
for r in results:
    boxes = r.boxes
    for box in boxes:

            conf = math.ceil((box.conf[0] * 100)) / 100
        

            # Class Name
            cls = int(box.cls[0])
            label = classNames[cls]
            detected_labels.append(label)

            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


print(detected_labels)
for item in detected_labels:
 pos_system.detect_item(item)
# Compare scanned items with detected items
print("Scanned items:", pos_system.scanned_items)
print("Detected items:", pos_system.detected_items)