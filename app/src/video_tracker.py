import cv2 
import requests
import json
import numpy as np
import time

from datetime import datetime


class VideoTracker:

    def __init__(self, url: str, interval: int) -> None:
        self.url = url
        self.interval = interval
        
        self.vid = cv2.VideoCapture(0)

        print(self.vid)

    def loop(self):
        start_time = time.time()
        
        while(True): 
            _, frame = self.vid.read() 
            
            #cv2.imshow('frame', frame) 

            current_time = time.time()

            # Check if the interval has elapsed
            if current_time - start_time >= self.interval:
                
                self.send_frame(frame)
                
                start_time = time.time()

            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break

    def send_frame(self, frame):
        json_to_send = {
            "frame": frame.tolist(),
            "datetime": int(datetime.timestamp(datetime.now()))
        }

        requests.post(url=self.url, json=json_to_send)