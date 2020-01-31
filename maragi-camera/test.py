import cv2
from maragi import Client
from time import time, sleep


class Microservice():
    def __init__(self, fps=1, ip='127.0.0.1', port='9999'):
        self.fps = fps
        self.client = Client(ip=ip, port=port)
    
    def _transmit_loop(self):
        cap = cv2.VideoCapture(0)
        while True:
            start = time()
            ret, frame = cap.read()
            self.client.send(frame.tolist())
            elapsed = time() - start
            delay = 1.0 / self.fps - elapsed
            sleep(delay)
    
    def run(self):
        self.thread = threading.Thread(target=self._transmit_loop)
        self.thread.start()

    def status(self):
        print('running:', self.thread.isAlive())
        return self.thread.isAlive()

    def stop(self):
        self.thread.terminate()
        
    def original(self):
        cap = cv2.VideoCapture(0)
        while True:
            start = time()
            ret, frame = cap.read()
            self.client.send(frame.tolist())
            elapsed = time() - start
            delay = 1.0 / self.fps - elapsed
            sleep(delay)        