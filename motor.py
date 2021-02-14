import serial
import time


def yazdir(komut):
    # Open grbl serial port
    # buraya com port bulan bir function ekle!!!
    cnc = serial.Serial('COM3', 115200, timeout=200.00)
    if komut == 50:
        # Open g-code file
        f = open('gcodes/bostablo.gcode', 'r')



    elif komut == 0:
        # Open g-code file
        f = open('gcodes/refX0.txt', 'r')
    elif komut == 1:
        # Open g-code file
        f = open('gcodes/refX1.txt', 'r')
    elif komut==2:
        # Open g-code file
        f = open('gcodes/refX2.txt', 'r')
    elif komut==3:
        # Open g-code file
        f = open('gcodes/refX3.txt', 'r')
    elif komut==4:
        # Open g-code file
        f = open('gcodes/refX4.txt', 'r')
    elif komut==5:
        # Open g-code file
        f = open('gcodes/refX5.txt', 'r')
    elif komut==6:
        # Open g-code file
        f = open('gcodes/refX6.txt', 'r')
    elif komut==7:
        # Open g-code file
        f = open('gcodes/refX7.txt', 'r')
    elif komut==8:
        # Open g-code file
        f = open('gcodes/refX8.txt', 'r')


    elif komut == 9:
        # Open g-code file
        f = open('gcodes/refO0.txt', 'r')
    elif komut == 10:
        # Open g-code file
        f = open('gcodes/refO1.txt', 'r')
    elif komut == 11:
        # Open g-code file
        f = open('gcodes/refO2.txt', 'r')
    elif komut == 12:
        # Open g-code file
        f = open('gcodes/refO3.txt', 'r')
    elif komut == 13:
        # Open g-code file
        f = open('gcodes/refO4.txt', 'r')
    elif komut == 14:
        # Open g-code file
        f = open('gcodes/refO5.txt', 'r')
    elif komut == 15:
        # Open g-code file
        f = open('gcodes/refO6.txt', 'r')
    elif komut == 16:
        # Open g-code file
        f = open('gcodes/refO7.txt', 'r')
    elif komut == 17:
        # Open g-code file
        f = open('gcodes/refO8.txt', 'r')

    elif komut == 18:
        # Open g-code file
        f = open('gcodes/w02.txt', 'r')
    elif komut == 19:
        # Open g-code file
        f = open('gcodes/w06.txt', 'r')
    elif komut == 20:
        # Open g-code file
        f = open('gcodes/w08.txt', 'r')
    elif komut == 21:
        # Open g-code file
        f = open('gcodes/w17.txt', 'r')
    elif komut == 22:
        # Open g-code file
        f = open('gcodes/w28.txt', 'r')
    elif komut == 23:
        # Open g-code file
        f = open('gcodes/w35.txt', 'r')
    elif komut == 24:
        # Open g-code file
        f = open('gcodes/w62.txt', 'r')
    elif komut == 25:
        # Open g-code file
        f = open('gcodes/w68.txt', 'r')

    # Wake up grbl
    cnc.write("\r\n\r\n".encode('utf-8'))
    time.sleep(2)  # Wait for grbl to initialize
    cnc.flushInput()  # Flush startup text in serial input

    # Stream g-code to grbl
    for line in f:
        l = line.strip()  # Strip all EOL characters for streaming
        #print('Sending: ' + l)
        cnc.write((l + '\n').encode('ascii'))  # Send g-code block to grbl
        grbl_out = cnc.readline().decode('ascii');  # Wait for grbl response with carriage return
        #print(grbl_out.strip())

    # Wait here until grbl is finished to close serial port and file.
    # raw_input("  Press <Enter> to exit and disable grbl.")

    # Close file and serial port
    f.close()
    cnc.close()