import time
import requests

import pygame
import pygame.camera

from datetime import datetime

from typing import Tuple

from PIL import Image
from io import BytesIO


class PyGameVideoTracker:

    def __init__(self, url: str, interval: int, window_size: Tuple[int] = (640, 480)) -> None:
        self.url = url
        self.interval = interval
        
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
        start_time = time.time()

        while True:
            frame = self.cam.get_image()

            current_time = time.time()

            if current_time - start_time >= self.interval:
                
                status_code = self.send_frame(frame)

                print(status_code)
                
                start_time = time.time()

    def send_frame(self, frame):
        frame = pygame.image.tostring(frame, "RGB")
        frame = Image.frombytes("RGB", self.window_size, frame)

        print(frame)

        frame_byte_arr = BytesIO()
        frame.save(frame_byte_arr, format="PNG")
        frame_byte_arr.seek(0)

        response = requests.post(url=self.url + "/receiveFrame", files={
            "file": frame_byte_arr
        })

        return response.status_code

