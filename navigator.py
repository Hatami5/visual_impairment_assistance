"""
Navigation Logic for Visually Impaired Assistance
Decides LEFT / RIGHT / STOP / FORWARD based on detections
"""

class Navigator:
    def __init__(self,
                 danger_distance="near",
                 center_margin=0.15):
        """
        danger_distance: objects considered dangerous if too close
        center_margin: percentage of frame width considered "center"
        """
        self.danger_distance = danger_distance
        self.center_margin = center_margin

    def decide(self, detections, frame_shape):
        """
        detections: enriched detections with distance
        frame_shape: (H, W, C)
        returns: navigation instruction (str or None)
        """
        if not detections:
            return "Path is clear. Move forward."

        H, W, _ = frame_shape
        center_left = W * (0.5 - self.center_margin)
        center_right = W * (0.5 + self.center_margin)

        danger_center = False
        danger_left = False
        danger_right = False

        for det in detections:
            if det.get("distance") != self.danger_distance:
                continue

            x1, _, x2, _ = det["bbox"]
            obj_center = (x1 + x2) / 2

            if center_left <= obj_center <= center_right:
                danger_center = True
            elif obj_center < center_left:
                danger_left = True
            else:
                danger_right = True

        if danger_center:
            if not danger_left:
                return "Obstacle ahead. Move left."
            if not danger_right:
                return "Obstacle ahead. Move right."
            return "Stop. Obstacle very close."

        return "Path is clear. Move forward."
