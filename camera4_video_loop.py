import sys
import json
from picamera2 import Picamera2
from datetime import datetime

picam2 = Picamera2()


with open('../../parametros.json', 'r') as archivo:
	parametros = json.load(archivo)

print(parametros["clip_duration"])

deviceID=parametros["deviceID"]
clip_duration=parametros["clip_duration"]

a = 0
b=2023

while(1):
	now = datetime.now()
	dt_string = now.strftime("%Y%m%d_%H%M%S")
	picam2.start_and_record_video(f'../../videos/DS{deviceID:04d}_{dt_string}.mp4', duration=clip_duration)
	a=a+1
	print('aqui')
	
