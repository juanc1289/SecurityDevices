from datetime import datetime

a = 1
b = 2023

now = datetime.now()
dt_string = now.strftime("%Y%m%d_%H%M%S")
print(f'DS{a:04d}_{dt_string}')


file1 = open(f'../../ubicaciones/DS{a:04d}_{dt_string}.txt',"a")

file1.write("am")

file1.close()
