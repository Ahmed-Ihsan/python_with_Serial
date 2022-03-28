import serial
import time

print('connection with port ...')
ser = serial.Serial(port, 9800, timeout=1)
print(f'reading Data from port {port} ')

for i in range(50):
        line = ser.readline()# read a byte
        if line:
            string = line.decode()  # convert the byte string to a unicode string
            num = int(string) # convert the unicode string to an int
            print("Data is",end=': ')
            print(num)
            
ser.close()