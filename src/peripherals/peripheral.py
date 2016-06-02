import threading


class Peripheral(object):

    supported_firmwares = []
    commands = []

    def __init__(self, serial, firmware):
        self.pause_reading = False
        self.serial = serial
        self.firmware = firmware
        if self.firmware not in self.supported_firmwares:
            print(self.supported_firmwares)
            raise UnsupportedFirmwareException(self.firmware)
        self.create_read_thread()
        if hasattr(self, "commands_firmware_"+str(firmware)):  # use firmware-specific commands if provided
            self.commands = getattr(self, "commands_firmware_"+str(firmware))

    def start_reading(self):
        try:
            self.reading_thread.start()
        except RuntimeError:  # restart thread
            self.create_read_thread()
            self.reading_thread.start()

    def create_read_thread(self):
        self.stop_reading_evt = threading.Event()
        self.reading_thread = threading.Thread(target=self._read,
            name="Thread reading for peripheral {} at port {}".format(self.__class__.__name__, self.serial.name))

    def close(self):
        self.stop_reading_evt.set()
        self.serial.close()

    def _read(self):
        if not hasattr(self, "read"):
            self.read = ""
        self.char = None
        while not self.stop_reading_evt.is_set():
            self.char = self.serial.read(1)
            if self.char not in (b'\n', b'\r', b'#', b'?'):
                self.read += self.char.decode('utf-8')
            if self.char == b'\n':
                if self.read != '':
                    self.call_command(self.read)
                self.read = ""

    def call_command(self, command):
        splt = command.split()
        command_name = splt[0]
        command_args = splt[1:]
        called = False
        for com in self.commands:
            if com.name == command_name:
                com(*command_args, per=self)
                called = True
        if not called:
            print("Couldn't find command handler for {}".format(command))


    def write(self, string):
        if not string.endswith('\n'):
            string += '\n'
        self.serial.write(string.encode('utf-8'))


class Command(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        raise NotImplementedError("__call__ method not implemented in command '{}'.".format(self.name))


class UnsupportedFirmwareException(Exception):
    def __init__(self, firmware):
        self.firmware = firmware
        super().__init__("{}.".format(self.firmware))
