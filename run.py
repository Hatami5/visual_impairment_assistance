"""
Entry point for Offline Visual Assistant MVP
Run: python run.py
"""

import cv2
import time

from core.camera import Camera
from core.frame_manager import FrameManager
from core.pipeline import Pipeline
from core.detector import ObjectDetector


def main():
    camera = Camera(camera_id=0, width=320, height=240)
    frame_manager = FrameManager(target_fps=15)
    #detector = ObjectDetector(model_name="yolov8n.pt", confidence_threshold=0.5)


    pipeline = Pipeline(camera=camera, frame_manager=frame_manager)

    print("[INFO] Visual Assistant started. Press 'q' to exit.")

    while True:
        pipeline.step()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
