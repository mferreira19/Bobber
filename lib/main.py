#!/usr/bin/env python3

"""
Serial Helper for Bobber Project
Summer 2018
"""

import serial
import sys
from datetime import datetime

# this port address is for the serial tx/rx pins on the GPIO header
# SERIAL_PORT = '/dev/cu.usbmodem1421'
# be sure to set this to the same rate used on the Arduino
# SERIAL_RATE = 9600


def get_time():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]


def main():

    if len(sys.argv)== 4:
            SERIAL_PORT = sys.argv[1]
            BAUD_RATE   = int(sys.argv[2])
            FILENAME    = sys.argv[3]
    else:
        print("No serial port, baud rate, and filename provided")
        print("  USAGE: python3 main.py <serialport> <baudrate> <filename>")
        print("EXAMPLE: python3 main.py /dev/cu.usbmodem1421 9600 PH.csv")
        print("EXAMPLE: python3 main.py /dev/cu.usbmodem1422 9600 ORP.csv")
        sys.exit(1)

    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

    with open(FILENAME, "a") as filepointer:
        filepointer.write("%s,%s,%s\r\n" % ("time", "temp", "value"))

    while True:
        reading = ser.readline().decode('utf-8')
        parsed_line = reading.strip().split(",")

        time, temp, value = get_time(), parsed_line[0], parsed_line[1]

        with open(FILENAME, "a") as filepointer:
            filepointer.write("%s,%s,%s\r\n" % (time, temp, value))


if __name__ == "__main__":
    main()
