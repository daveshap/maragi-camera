import cv2
from maragi import Client
from time import time, sleep


class Microservice():
    def __init__(self, fps=1, client=Client())
        self.fps = fps
        self.client = Client()
        
    def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            start = time()
            ret, frame = cap.read()
            self.client.send(frame)
            elapsed = time() - start
            delay = 1.0 / self.fps - elapsed
            sleep(delay)
            