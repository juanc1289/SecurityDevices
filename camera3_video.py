import sys
from picamera2 import Picamera2
picam2 = Picamera2()
picam2.start_and_record_video(sys.argv[1]+".mp4", duration=int(sys.argv[2]))
