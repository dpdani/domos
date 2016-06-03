#    Copyright (C) 2016  Domos Group
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


import serial
import peripherals
from peripherals import peripheral
import threading

allowed_chars = [
    chr(x).encode() for x in range(32, 126)
]

unallowed_chars = [
    b'?', b'#', b'\n', b'\x00'
]


class UnknownPeripheralError(Exception):
    def __init__(self, model_code):
        super().__init__("cannot find peripheral named '{}'".format(model_code))


def keep_serials_updated(serials, peripherals):
    pass


def _recognize_serial(ser):
    per = peripheral.NotYetRecognizedPeripheral()
    thread = threading.Thread(target=_recognize_serial, args=(ser, per), name="Thread recognizing serial {}".format(ser))
    thread.start()
    return [per]


def recognize_serial(ser):
    char = None
    read = b""
    while not read.startswith(b'info'):
        ser.write(b"info\n")
        while char != b'\n':
            char = ser.read(1)
            if char in allowed_chars and char not in unallowed_chars:
                read += char
            if char == b'\n':
                print(read)
                break
    _, model_code, firmware_version = tuple(read.split(b' '))  # first is "info"
    model_code = model_code.decode('utf-8')
    firmware_version = int(firmware_version)
    try:
        exec("from peripherals import {} as periph".format(model_code), locals(), globals())
        return getattr(periph, model_code)(ser, firmware_version)
    except ImportError:
        raise UnknownPeripheralError(model_code)


def shish(asd='7'):
    ser = serial.Serial('/dev/ttyACM'+asd, 9600)
    return recognize_serial(ser)
