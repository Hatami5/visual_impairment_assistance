# core/frame_manager.py
import time


class FrameManager:
    def __init__(self, target_fps=10):
        self.target_interval = 1.0 / target_fps
        self.last_time = 0
        

    def should_process(self):
        now = time.time()
        if now - self.last_time >= self.target_interval:
            self.last_time = now
            return True
        return False
print("Frame_Manager run successfully")
    

        