import argparse

from src.video_tracker import PyGameVideoTracker

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument("--url")

args = parser.parse_args()
args = dict(args._get_kwargs())


video_tracker = PyGameVideoTracker(url=args["url"])

video_tracker.loop()