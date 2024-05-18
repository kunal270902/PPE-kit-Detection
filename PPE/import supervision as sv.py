import supervision as sv
from ultralytics import YOLO
import numpy as np

dataset = sv.DetectionDataset.from_yolo(
    annotations_directory_path='dataset/annotations.csv',  # Path to the directory containing annotations.csv
    data_yaml_path='dataset/data_custom.yaml',
    images_directory_path='dataset/train' # Set to None if you don't have a data.yaml file
)
model = YOLO('yolov8s_custom.pt')
def callback(image: np.ndarray) -> sv.Detections:
    result = model(image)[0]
    return sv.Detections.from_ultralytics(result)

confusion_matrix = sv.ConfusionMatrix.benchmark(
   dataset = dataset,
   callback = callback
)

confusion_matrix.plot()