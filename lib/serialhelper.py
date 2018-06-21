
# from serial import serial
import serial
from datetime import datetime
# this port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = '/dev/cu.usbmodem1411'
# be sure to set this to the same rate used on the Arduino
SERIAL_RATE = 9600

def gettime():
    return  (datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] )



def main():
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
    #filepointer = open("sensordata.txt", "w+")

    #filetime = (gettime()[0:13])

    print (gettime()[0:13])

#This is a section on creating a cache for the live data display It write
#It creates a file data.csv writes to an array and then removes the data after 20 lines are full



    while True:

        filetime = (gettime()[0:13])

        # using ser.readline() assumes each line contains a single reading
        # sent using Serial.println() on the Arduino
        reading = ser.readline().decode('utf-8')
        parsed_line = reading.strip().split(",")

        time, temp, humidity = gettime(), parsed_line[0], parsed_line[1]

        print(time, temp, humidity)


# this is the File naming system that uses the variable (filetime) to take the Year:Month:Day:Hour and write it to a csv file


        #with open("Sensordata" + str(filetime) + ".csv" , "a") as filepointer:


        with open('data.csv', "a") as filepointer:




            open("simple" + str(minLength) + str(minBF) + ".csv","w")



            filepointer.write("%s,%s,%s \r\n" % (time, temp, humidity))






if __name__ == "__main__":
    main()