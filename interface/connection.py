import serial
import time
import glob

ser = None #serial.Serial('COM7', 9600, timeout=1) #serial connection to arduino device

def read_response_from_arduino():
    response = ser.read()
    print(response.decode("ascii"))

#send each character in the command as a byte
def send_command_to_arduino(command):
    for char in command:
        ser.write(bytes(char, encoding='utf-8')) 
    ser.write(bytes('\n', encoding='utf-8')) #we are using the newline character to signal the command is complete

def main():
    print("Device booting...")
    time.sleep(2) #wait for arduino to bootup

    print("Welcome!")
    print("Select a file 2dCAD's drawing directory that you would like to draw..")

    files = glob.glob(r'..\app\drawings\*.cad')

    if files == []:
        print("Well there doesn't seem to be any....")
        print("You probably should go create some.")
    else:
        for r in range(len(files)):
            print(str(r) + ". " + files[r])

main()

