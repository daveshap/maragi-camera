import time
import cv2

class Camera:
    def __init__(self, service='camera', fps=1):
        self.servers = []  # TODO support multiple MARAGI servers
        self.cameras = []  # TODO support multiple cameras
        self.svc_name = service
        self.fps = fps
        self.delay = 1.0 / fps
        self.camera = cv2.VideoCapture(0)
        
    def camera_thread(self):
        # TODO enable threading (for multiple cameras, start/stop, etc)
        print('this is a fake camera thread')
    
    def start(self):
        # TODO switch to threading
        metadata = {'datatype': 'numpy', 'type': 'image'}
        while True:
            last_cap = time.time()
            ret, frame = self.camera.read()
            print('pretending to send image', frame.shape, 'last time', last_cap)
            time.sleep(self.delay)
            
    
    def list_cameras(self):
        # TODO
        print('the following cameras are available...')
      
    def claim_camera(self, cam_id=0):
        # TODO 
        print('Claimed camera', cam_id)
