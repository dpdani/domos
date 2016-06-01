import serial
import peripherals


def recognize_serial(ser):
    ser.write("info\n")
    char = None
    read = ""
    while char != '\n':
        char = ser.read(1)
        if char not in ('#', '\n'):
            read += char
    _, model_code, firmware_version = tuple(read.split(' '))  # first is "info"
    firmware_version = int(firmware_version)

