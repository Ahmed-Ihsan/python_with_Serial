import serial
import time
import sys
import glob

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
       
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
    if len(result) > 1:
        for i in enumerate(result):
            print(f'port --> {i[0]}: {i[1]}')
        while True:
            input_uesr = input('enter port number: \n >> ')
            if type(input_uesr) is str:
                port = result[int(input_uesr)]
                break
            
    else:
        port = result[0]
        
    print(port)
    ser = serial.Serial(port, 9600, timeout=1)
    return ser

def rec_data(ser):
    for i in range(50):
        line = ser.readline()
        if line:
            string = line.decode()  
            num = string
            print(num)
    return num

port = serial_ports()
while True:
    rec_data(port)
port.close()