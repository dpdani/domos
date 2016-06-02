import peripherals.peripheral as peripheral


class UnrecognizedCommand(peripheral.Command):
    def __init__(self):
        super().__init__('unrecognized_command')

    def __call__(self, *args, **kwargs):
        del kwargs['per']
        print("UNRECOGNIZED COMMAND: ", *args, **kwargs)

class Info(peripheral.Command):
    def __init__(self):
        super().__init__('info')

    def __call__(self, *args, **kwargs):
        del kwargs['per']
        print("INFO COMMAND: ", *args, **kwargs)


class Temperature(peripheral.Command):
    def __init__(self):
        super().__init__('temperature')

    def __call__(self, *args, **kwargs):
        del kwargs['per']
        print("TEMPERATURE: ", *args, **kwargs)


class ToggleLed(peripheral.Command):
    def __init__(self):
        super().__init__('toggle_led')

    def __call__(self, *args, **kwargs):
        print("TOGGLE LED.")


class ButtonIs(peripheral.Command):
    def __init__(self):
        super().__init__('button_is')

    def __call__(self, *args, **kwargs):
        del kwargs['per']
        print("BUTTON IS: ", *args, **kwargs)


class ButtonPressed(peripheral.Command):
    def __init__(self):
        super().__init__('button_pressed')

    def __call__(self, *args, **kwargs):
        print("BUTTON PRESSED. toggling led.")
        kwargs['per'].write("toggle_led")


class DoorOpened(peripheral.Command):
    def __init__(self):
        super().__init__('door_opened')

    def __call__(self, *args, **kwargs):
        print("DOOR OPENED. toggling led.")
        kwargs['per'].write("toggle_led")


class DoorClosed(peripheral.Command):
    def __init__(self):
        super().__init__('door_closed')

    def __call__(self, *args, **kwargs):
        print("DOOR CLOSED. toggling led.")
        kwargs['per'].write("toggle_led")
