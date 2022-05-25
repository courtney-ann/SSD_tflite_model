import serial
import time,sys
from datetime import datetime

SERIAL_PORT = "/dev/ttyS0"
ser=serial.Serial(SERIAL_PORT, baudrate=9600)

def millis():
    milliSeconds=int(round(time.time()*1000))
    return milliSeconds

def sendTabData(command, timeout,debug):
    ser.write(command)
    t = millis()
    i=0
    
    while (t+timeout)>millis():
        while ser.inWaiting():
            
            dat=""
            c=ser.readline()
            a=c.decode()
                
            x = "+CGNSINF:" in a
            if x:
                b=(a.split(","))
                state=b[1]
                latitude=b[3]
                longitude=b[4]
                
                return state,latitude,longitude
DEBUG=True
ser.write((b'AT+CSMP=17,167,0,0'+b'\r\n'))
time.sleep(0.1)
ser.write((b'AT+CMGF=1'+b'\r\n'))
time.sleep(0.4)
ser.write((b'AT+CGNSPWR=1'+b'\r\n'))
time.sleep(0.05)
ser.write((b'AT+CGNSSEQ=RMC'+b'\r\n'))
time.sleep(0.15)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
now = datetime.today()
date = now.strftime("%d/%m/%y")
while True:
    stat,lat,long=sendTabData(b'AT+CGNSINF'+b'\r\n',1000,DEBUG)
    if stat=="1":
        print(f"latitude: {lat}")
        print(f"longitude: {long}")
        print(f"time: {current_time}")
        print(f"date: {date}")

