"""
Heuristic Distance Estimation (CPU-friendly)
Estimates distance based on bounding box size
"""

class DistanceEstimator:
    def __init__(self,
                 frame_width=640,
                 near_threshold=0.35,
                 medium_threshold=0.20):
        """
        near_threshold / medium_threshold are ratios of bbox area to frame area
        """
        self.frame_area = frame_width * frame_width
        self.near_th = near_threshold
        self.med_th = medium_threshold

    def estimate(self, detections, frame_shape):
        """
        detections: list of detection dicts
        frame_shape: (H, W, C)
        returns: detections with distance info
        """
        frame_area = frame_shape[0] * frame_shape[1]
        enriched = []

        for det in detections:
            x1, y1, x2, y2 = det["bbox"]
            bbox_area = max(1, (x2 - x1) * (y2 - y1))
            ratio = bbox_area / frame_area

            if ratio >= self.near_th:
                distance = "near"
            elif ratio >= self.med_th:
                distance = "medium"
            else:
                distance = "far"

            det_copy = det.copy()
            det_copy["distance"] = distance
            det_copy["area_ratio"] = round(ratio, 3)
            enriched.append(det_copy)

        return enriched
