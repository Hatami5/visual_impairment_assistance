"""
Offline Speech-to-Text (Voice Commands)
Uses VOSK for reliable CPU-only offline recognition
"""

import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer


class CommandListener:
    def __init__(self,
                 model_path="models/stt/vosk",
                 sample_rate=16000):
        self.sample_rate = sample_rate
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, sample_rate)
        self.audio_queue = queue.Queue()

    def _callback(self, indata, frames, time, status):
        if status:
            return
        self.audio_queue.put(bytes(indata))

    def listen_once(self):
        """
        Listens briefly and returns a command string or None
        """
        with sd.RawInputStream(
            samplerate=self.sample_rate,
            blocksize=8000,
            dtype='int16',
            channels=1,
            callback=self._callback
        ):
            try:
                data = self.audio_queue.get(timeout=0.5)
            except queue.Empty:
                return None

            if self.recognizer.AcceptWaveform(data):
                result = json.loads(self.recognizer.Result())
                text = result.get("text", "").lower()
                return text if text else None

        return None
