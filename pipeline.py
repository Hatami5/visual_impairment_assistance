# core/pipeline.py
import cv2
from core.detector import ObjectDetector
from core.distance_estimator import DistanceEstimator
from core.scene_reasoner import SceneReasoner
from core.speaker import Speaker
from core.command_listener import CommandListener
from core.navigator import Navigator


class Pipeline:
    def __init__(self, camera, frame_manager):
        self.camera = camera
        self.frame_manager = frame_manager
        self.detector = ObjectDetector()
        self.distance_estimator = DistanceEstimator()
        self.reasoner = SceneReasoner()
        self.speaker = Speaker()
        self.listener = CommandListener()
        self.navigator = Navigator()


    def step(self):
        frame = self.camera.read()
        if frame is None:
            return
         # Listen for voice command (non-blocking)
        command = self.listener.listen_once()
        if command:
            print("[COMMAND]", command)
            if "stop" in command:
                self.speaker.speak("Stopping guidance")
                return
            if "what" in command or "ahead" in command:
                self.speaker.speak("Analyzing scene ahead")


        if not self.frame_manager.should_process():
            return

        detections = self.detector.detect(frame)
        detections = self.distance_estimator.estimate(detections, frame.shape)
        navigation_msg = self.navigator.decide(detections, frame.shape)
        if navigation_msg:
            self.speaker.speak(navigation_msg)


        # Visual debug (can be removed later)
        for det in detections:
            x1, y1, x2, y2 = det["bbox"]
            label = det["label"]
            distance = det["distance"]

            color = (0, 255, 0)
            if distance == "near":
                color = (0, 0, 255)
            elif distance == "medium":
                color = (0, 165, 255)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(
                frame,
                f"{label} | {distance}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                color,
                2
            )

        cv2.imshow("Visual Assistant", cv2.resize(frame, (640, 480)))
