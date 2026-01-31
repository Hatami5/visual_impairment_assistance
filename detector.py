"""
CPU-only Object Detector
Uses YOLOv8 Nano (lightweight)
"""

import torch
from ultralytics import YOLO
# Suppose we want to store the model in "./yolo_models"
local_model_path = "yolov8n.pt"

class ObjectDetector:
    def __init__(
        self,
        model_name=local_model_path,
        confidence_threshold=0.6
           
    ):
        self.device = "cpu"
        torch.set_num_threads(1)

        self.model = YOLO(model_name)
        self.confidence_threshold = confidence_threshold

    def detect(self, frame):
        """
        frame: OpenCV BGR image
        returns: list of detections
        """

        results = self.model(
            frame,
            conf=self.confidence_threshold,
            device=self.device,
            verbose=False
        )

        detections = []

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                score = float(box.conf[0])
                cls_id = int(box.cls[0])

                detections.append({
                    "label": self.model.names[cls_id],
                    "score": score,
                    "bbox": [x1, y1, x2, y2]
                })

        return detections
print("Object_Detector run successfully") 