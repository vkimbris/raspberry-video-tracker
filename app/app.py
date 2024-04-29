import argparse

from src.video_tracker import VideoTracker

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument("--url")
parser.add_argument("--interval")

args = parser.parse_args()
args = dict(args._get_kwargs())


video_tracker = VideoTracker(url=args["url"], interval=int(args["interval"]))

video_tracker.loop()