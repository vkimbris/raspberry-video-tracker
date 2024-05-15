import time
import requests

import pygame
import pygame.camera

from datetime import datetime

from typing import Tuple


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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break

            frame = self.cam.get_image()

            current_time = time.time()

            if current_time - start_time >= self.interval:
                
                status_code = self.send_frame(PyGameVideoTracker.convert_frame_to_list(frame))

                print(status_code)
                
                start_time = time.time()

            self.screen.blit(frame, (0, 0))

            pygame.display.flip()

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
