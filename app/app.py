from src.video_tracker import VideoTracker


URL = "http://localhost:8000"
INTERVAL = 3


video_tracker = VideoTracker(url=URL, interval=INTERVAL)


video_tracker.loop()