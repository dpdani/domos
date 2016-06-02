import peripherals.peripheral as peripheral


class UnrecognizedCommand(peripheral.Command):
    def __init__(self):
        super().__init__('unrecognized_command')

    def __call__(self, *args, **kwargs):
        print("UNRECOGNIZED COMMAND: ", *args, **kwargs)

class Info(peripheral.Command):
    def __init__(self):
        super().__init__('info')

    def __call__(self, *args, **kwargs):
        print("INFO COMMAND: ", *args, **kwargs)


class Temperature(peripheral.Command):
    def __init__(self):
        super().__init__('temperature')

    def __call__(self, *args, **kwargs):
        print("TEMPERATURE: ", *args, **kwargs)