import serial
import threading

import time

DEFAULT_BAUDRATE = 9600
DEFAULT_PORTS = [
    'COM1',
    'COM2',
    'COM3',
    'COM4',
]


def start_listening(ports=DEFAULT_PORTS):
    stop_event = threading.Event()
    threads = []
    serials = []
    for port in ports:
        thread = threading.Thread(target=listen_port, args=(port, stop_event, serials),
                                  name='Thread listening on port {}'.format(port))
        thread.start()
        threads.append(thread)
    return threads, serials, stop_event


def listen_port(port, stop_event, serials, baudrate=DEFAULT_BAUDRATE):
    while not stop_event.is_set():
        try:
            ser = serial.Serial(port, baudrate)
        except serial.SerialException as exc:
            continue
        serials.append(ser)
        print("Found somebody at {}".format(port))
        return ser



if __name__ == '__main__':
    print("--- TESTING MODULE 'ports_listener.py'")
    threads, serials, stop_event = start_listening()
    _threads, _serials, _stop_event = None, None, None
    while True:
        if _threads != threads or _serials != serials or _stop_event != stop_event:
            print(threads, serials, stop_event)
        _threads, _serials, _stop_event = threads.copy(), serials.copy(), stop_event
        if len(serials) > 0:
            stop_event.set()
            break
