import serial
import time
import sys
import glob
import keyboard
import threading
import requests

def main():
    def serial_ports():
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                print(s.dtr)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

    port = serial_ports()
    print(port)
    if len(port) > 1:
        while True:
            input_uesr = input('enter port name: like COM3 \n >> ')
            if type(input_uesr) is str:
                index = port.index(input_uesr)
                port = port[index]
                break
    else:
        port = port[0]
        
    # make sure the 'COM#' is set according the Windows Device Manager
    print('connection with port ...')
    ser = serial.Serial(port, 9800, timeout=1)
    print(f'reading Data from port {port} ')
    stop = False
    while True :
        for i in range(50):
            line = ser.readline()# read a byte
            if line:
                string = line.decode()  # convert the byte string to a unicode string
                num = string
                print("Data is",end=': ')
                requests.post(f'http://127.0.0.1:5002/updateData/{num}')
                print(num)
            if keyboard.is_pressed("s"):
                stop =True
                break
        if stop:
            break
        
    ser.close()

t1 = threading.Thread(target = main)
t1.start()