import peripherals.peripheral as peripheral
import peripherals.commands as commands


class TEMP001(peripheral.Peripheral):
    supported_firmwares = [100]
    commands = [
        commands.UnrecognizedCommand(),
        commands.Info(),
        commands.Temperature(),
    ]
