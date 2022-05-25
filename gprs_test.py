import serial
import time,sys
from datetime import datetime

SERIAL_PORT = "/dev/ttyS0"
ser=serial.Serial(SERIAL_PORT, baudrate=9600)

def gprs_http_post(postData):
    ser.write((b'AT+CFUN=1'+b'\r\n'))
    time.sleep(0.5)
    ser.write((b'AT+SAPBR=1,1'+b'\r\n'))                 #start connection
    time.sleep(0.5)
    ser.write((b'AT+SAPBR=2,1'+b'\r\n'))
    time.sleep(5)
    ser.write((b'AT+HTTPINIT'+b'\r\n'))                  #enable http mode
    time.sleep(0.5)
    ser.write((b'AT+HTTPPARA=CID,1'+b'\r\n'))                 #attach gprs
    time.sleep(0.5)
    ser.write((b'AT+HTTPPARA=URL,http://testserver.aeq-web.com/sim800_test/sim800.php?param=TestFromMySim800'+b'\r\n'))
    time.sleep(0.5)
    #ser.write((b'AT+HTTPPARA=CONTENT,application/json'+b'\r\n'))
    ser.write((b'AT+HTTPPARA=CONTENT,application/x-www-form-urlencoded'+b'\r\n'))
    time.sleep(0.5)
    ser.write((b'AT+HTTPDATA={len(postData)},10000'+b'\r\n'))              #Tells the module that you will be sending 192 bytes of data and it can timeout after 10 seconds of inactivity. After this command you get the DOWNLOAD URC then you can type in 192 bytes of data within 10 seconds. 
    time.sleep(2)
    ser.write(postData)
    time.sleep(3)
    ser.write((b'AT+HTTPACTION=1'+b'\r\n'))
    time.sleep(1)
    ser.write((b'AT+HTTPREAD'+b'\r\n'))
    time.sleep(1)
    ser.write((b'AT+HTTPTERM'+b'\r\n'))
    time.sleep(0.5)
    
    
def gsm_config_gprs():
    ser.write((b'AT+SAPBR=3,1,Contype,GPRS'+b'\r\n'))
    time.sleep(0.05)
    ser.write((b'AT+SAPBR=3,1,APN,web.digiceljamaica.com'+b'\r\n'))     #set apn
    time.sleep(0.05)
    ser.write((b'AT+SAPBR=3,1,USER,LMT'+b'\r\n'))       #set user
    time.sleep(0.05)
    ser.write((b'AT+SAPBR=3,1,PWD,wap03jam'+b'\r\n'))    #set password
    time.sleep(0.05)
 
#debug this function 
def gprs_http_get(url):
    ser.write((b'AT+CFUN=1'+b'\r\n'))
    time.sleep(0.5)
    ser.write((b'AT+SAPBR=1,1'+b'\r\n'))                 #start connection
    time.sleep(0.5)
    ser.write((b'AT+SAPBR=2,1'+b'\r\n'))
    time.sleep(5)
    ser.write((b'AT+HTTPINIT'+b'\r\n'))                  #enable http mode
    time.sleep(0.5)
    ser.write((b'AT+HTTPPARA=CID,1'+b'\r\n'))                 #attach gprs
    time.sleep(0.5)
    ser.write((b'AT+HTTPPARA=URL,{url}'+b'\r\n'))
    time.sleep(0.5)
    ser.write((b'AT+HTTPACTION=0'+b'\r\n'))
    time.sleep(1)
    ser.write((b'AT+HTTPREAD'+b'\r\n'))
    time.sleep(1)
    ser.write((b'AT+HTTPTERM'+b'\r\n'))
    time.sleep(0.5)    


for i in range (1):
    gsm_config_gprs()
    gprs_http_post(b'param=TestFromMySim800'+b'\r\n')
    #gprs_http_get(b'http://testserver.aeq-web.com/sim800_test/sim800.php?param=TestFromMySim800')
    ser.write((b'AT+SAPBR=0,1'+b'\r\n')) 
    
    

    

    