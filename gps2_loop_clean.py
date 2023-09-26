import serial
import time 
import json
from datetime import datetime

WAV_13460 = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=2.0)

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

while(1):
	now = datetime.now()
	dt_string = now.strftime("%Y%m%d_%H%M%S")
	file1 = open(f'../../ubicaciones/DS{deviceID:04d}_{dt_string}.txt',"a")
	for a in range(0,clip_duration):
		message='AT+CGNSINF\r\n'
		message_utf= message.encode(encoding='utf-8', errors = 'strict')
		WAV_13460.write(message_utf)
		result=WAV_13460.read(100)
		print(result)
		file1.write(str(result,encoding = 'utf-8'))
		time.sleep(2)	
	
	print('aqui')
	file1.close()




