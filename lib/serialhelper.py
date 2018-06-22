
# from serial import serial
import serial
# from serial import *
from datetime import datetime

import sys

# this port address is for the serial tx/rx pins on the GPIO header
# SERIAL_PORT = '/dev/cu.usbmodem1421'
# be sure to set this to the same rate used on the Arduino
# SERIAL_RATE = 9600

def gettime():
    return  (datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] )


def main():

    if len(sys.argv)== 3:
            SERIAL_PORT = sys.argv[1]
            BAUD_RATE = sys.argv[2]
    else:

        print("No serial port and baud rate provided")
        print("  USAGE: python3 serialhelper.py <serialport> <baudrate>")
        print("EXAMPLE: python3 serialhelper.py /dev/cu.usbmodem1421 9600")
        sys.exit(1)

    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

    #This is a section on creating a cache for the live data display It write
    #It creates a file data.csv writes to an array and then removes the data after 20 lines are full

    with open('../HTML/data.csv', "a") as filepointer:
        filepointer.write("%s,%s,%s\r\n" % ("time", "temp", "hum"))


    while True:

        # using ser.readline() assumes each line contains a single reading
        # sent using Serial.println() on the Arduino
        reading = ser.readline().decode('utf-8')
        parsed_line = reading.strip().split(",")

        time, temp, humidity = gettime(), parsed_line[0], parsed_line[1]

        with open('../HTML/data.csv', "a") as filepointer:
            filepointer.write("%s,%s,%s \r\n" % (time, temp, humidity))



if __name__ == "__main__":
    main()