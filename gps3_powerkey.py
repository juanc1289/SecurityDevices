import serial
import time
import RPi.GPIO as GPIO
import json
from datetime import datetime


GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
while True:
	GPIO.output(7, GPIO.LOW)
	time.sleep(4)
	GPIO.output(7, GPIO.HIGH)
	break
print('hereeeeee')
GPIO.cleanup()


WAV_13460 = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=0.5)

with open('../../parametros.json', 'r') as archivo:
	parametros = json.load(archivo)

print(parametros["clip_duration"])

deviceID=parametros["deviceID"]
clip_duration=parametros["clip_duration"]

message='AT+CGNSPWR=1\r\n'
message_utf= message.encode(encoding='utf-8', errors = 'strict')

WAV_13460.write(message_utf)
result=WAV_13460.read(150)
print(result)


for c in range(0,8):
	result=WAV_13460.readline()
	print(f'line c = {c}',result)
	time.sleep(0.5)
while(1):
	now = datetime.now()
	dt_string = now.strftime("%Y%m%d_%H%M%S")
	file1 = open(f'../../ubicaciones/DS{deviceID:04d}_{dt_string}.txt',"a")
	for a in range(0,clip_duration):
		message='AT+CGNSINF\r\n'
		message_utf= message.encode(encoding='utf-8', errors = 'strict')
		WAV_13460.write(message_utf)
		#result=WAV_13460.read(150)

		for b in range(0,4):
			result=WAV_13460.readline()
			print(f'line b = {b}',result)
			
			if(result[0]==43):
				print(f'line p = {b}',result)
				data = result.split(b',')
				print('data = ',data[2],data[3],data[4])
				file1.write(str(data[2]+b','+data[3]+b','+data[4]+b'\r\n',encoding = 'utf-8'))
				time.sleep(0.1)
		time.sleep(0.9)	
	
	print('aqui')
	file1.close()

