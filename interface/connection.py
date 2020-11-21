import serial
import time

ser = serial.Serial('COM7', 9600, timeout=10)
time.sleep(2) #wait for arduino to bootup

#send each character in the command as a byte
def send_command(command):
    for char in command:
        ser.write(bytes(char, encoding='utf-8')) 
    ser.write(bytes('\n', encoding='utf-8'))

send_command("LOW")