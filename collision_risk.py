"""
Collision Risk Analyzer
Detects imminent collision threats and generates urgent warnings
Designed for visually impaired navigation assistance
"""

class CollisionRiskAnalyzer:
    def __init__(self):
        # Objects that can cause physical collision
        self.danger_objects = {
            "person",
            "car",
            "bus",
            "bicycle",
            "motorcycle",
            "chair",
            "table",
            "wall",
            "door",
            "stairs",
        }

    def assess(self, detections, frame_shape):
        """
        detections: list of dicts with keys [label, bbox, distance]
        frame_shape: (H, W, C)
        returns: urgent warning string or None
        """
        if not detections:
            return None

        H, W, _ = frame_shape

        for det in detections:
            label = det.get("label")
            distance = det.get("distance")
            x1, _, x2, _ = det.get("bbox")

            # Only care about dangerous objects
            if label not in self.danger_objects:
                continue

            # Only trigger on near objects
            if distance != "near":
                continue

            # Check if object is in walking path (center of frame)
            center_x = (x1 + x2) / 2
            if W * 0.35 <= center_x <= W * 0.65:
                return f"Warning! {label} directly ahead"

        return None
