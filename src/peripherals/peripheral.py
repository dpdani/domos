import threading


class Peripheral(object):

    supported_firmwares = []

    def __init__(self, serial, firmware):
        self.serial = serial
        self.firmware = firmware
        if self.firmware not in self.supported_firmwares:
            raise UnsupportedFirmwareException(self.firmware)
        self.stop_reading_evt = threading.Event()
        self.reading_thread = threading.Thread(target=self._read,
            name="Thread reading for peripheral {} at port {}".format(self.__class__.__name__, serial.name))

    def start_reading(self):
        self.reading_thread.start()

    def _read(self):
        read = ""
        char = None
        while not self.stop_reading_evt.is_set():
            char = self.serial.read(1)
            if char not in ('\n', '#'):
                read += char
            if char == '\n':
                self.call_command(read)
                read = ""

    def call_command(self, command):
        pass

    def write(self, string):
        if not string.endswith('\n'):
            string += '\n'
        self.serial.write(string)


class UnsupportedFirmwareException(Exception):
    def __init__(self, firmware):
        self.firmware = firmware
        super().__init__("{}.".format(self.firmware))
