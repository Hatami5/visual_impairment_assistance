# core/speaker.py
import subprocess
import time


class Speaker:
    def __init__(self, cooldown_sec=4.5):
        self.cooldown_sec = cooldown_sec
        self._last_spoken = 0.0

    def _cooldown_ok(self):
        return (time.time() - self._last_spoken) >= self.cooldown_sec

    def speak(self, text: str):
        if not text or not self._cooldown_ok():
            return

        try:
            self._last_spoken = time.time()

            command = f'''
            Add-Type -AssemblyName System.Speech;
            $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer;
            $speak.Speak("{text}");
            '''

            subprocess.run(
                ["powershell", "-Command", command],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except Exception:
            pass
