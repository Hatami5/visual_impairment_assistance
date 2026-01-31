class SceneReasoner:
    def __init__(self):
        self.priority = [
            "person", "car", "bus", "bicycle", "motorcycle",
            "chair", "table", "stairs", "door"
        ]

    def _direction(self, bbox, frame_w):
        x1, _, x2, _ = bbox
        center_x = (x1 + x2) / 2

        if center_x < frame_w * 0.33:
            return "left"
        elif center_x > frame_w * 0.66:
            return "right"
        else:
            return "ahead"

    def decide(self, detections, frame_shape):
        if not detections:
            return None

        H, W, _ = frame_shape
        from collections import defaultdict
        buckets = defaultdict(list)

        for det in detections:
            buckets[det["label"]].append(det)

        for label in self.priority:
            if label in buckets:
                target = sorted(
                    buckets[label],
                    key=lambda d: (d["distance"] != "near", d.get("area_ratio", 0)),
                    reverse=True
                )[0]

                direction = self._direction(target["bbox"], W)
                distance = target["distance"]

                if distance == "near":
                    return f"{label} very close on your {direction}"
                elif distance == "medium":
                    return f"{label} ahead on your {direction}"
                else:
                    return f"{label} far away on your {direction}"

        return None
