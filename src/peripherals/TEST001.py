import peripherals.peripheral as peripheral
import peripherals.commands as commands


class TEST001(peripheral.Peripheral):
    supported_firmwares = [100]
    commands = [
        commands.UnrecognizedCommand(),
        commands.Info(),
        commands.ToggleLed(),
        commands.ButtonIs(),
    ]
