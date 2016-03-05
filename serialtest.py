import serial
import time
import commands

status,output = commands.getstatusoutput("ls /dev/ttyACM*")
ser = serial.Serial(output, 9600)  
time.sleep(3)
ser.write("r")
time.sleep(0.5)
print "turn right"
ser.write("r")
time.sleep(0.5)
print "turn right"
ser.write("r")
time.sleep(0.5)
print "turn right"
ser.write("r")
time.sleep(0.5)
print "turn right"
ser.write("r")
time.sleep(0.5)
print "turn right"
ser.write("r")
time.sleep(0.5)
print "turn right"
ser.write("r")
time.sleep(0.5)
time.sleep(3)
ser.write("l")
time.sleep(0.5)
print "turn left"
ser.write("l")
time.sleep(0.5)
print "turn left"
ser.write("l")
time.sleep(0.5)
print "turn left"
ser.write("l")
time.sleep(0.5)
print "turn left"
ser.write("l")
time.sleep(0.5)
print "turn left"
ser.write("l")
time.sleep(0.5)
print "turn left"
ser.write("l")
time.sleep(0.5)
ser.close()      
