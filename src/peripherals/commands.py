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
