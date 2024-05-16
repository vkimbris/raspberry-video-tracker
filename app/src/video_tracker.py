import time
import requests

import pygame
import pygame.camera

from datetime import datetime

from typing import Tuple


class PyGameVideoTracker:

    def __init__(self, url: str,  window_size: Tuple[int] = (640, 480)) -> None:
        self.url = url
        
        pygame.init()
        pygame.camera.init()
        
        self.window_size = window_size
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Webcam Feed")

        camlist = pygame.camera.list_cameras()
        if not camlist:
            raise ValueError("No cameras found")
        
        self.cam = pygame.camera.Camera(camlist[0], window_size)
        self.cam.start()

    def loop(self):
        while True:
            frame = self.cam.get_image()
                
            status_code = self.send_frame(PyGameVideoTracker.convert_frame_to_list(frame))

            print(status_code)
            

    def send_frame(self, frame):
        json_to_send = {
            "frame": frame,
            "datetime": int(datetime.timestamp(datetime.now())) 
        }

        response = requests.post(url=self.url + "/receiveImage", json=json_to_send)

        return response.status_code

    @staticmethod
    def convert_frame_to_list(frame):
        return pygame.surfarray.array3d(frame).tolist()
