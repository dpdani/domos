import ports_listener
from serial_recognizer import recognize_serial


def main():
    print("Waiting for peripherals to connect...")
    threads, serials, stop_event = ports_listener.loop_start_listening()

    peripheral_in_use = None
    peripheral_names = update_peripherals(serials)
    _serials = serials.copy()

    while True:
        if _serials != serials:
            new_peripherals = update_peripherals(serials - _serials)
            for periph in new_peripherals.values():
                peripheral_names.update({
                    len(peripheral_names): periph
                })  # ID: periph

        if peripheral_in_use is None:
            inp = input("Please choose a peripheral to work with ('list'): ")
            if inp in ('exit', 'quit', 'q'):
                stop_event.set()
                break
            elif inp in peripheral_names.keys():
                peripheral_in_use = inp
            elif inp == 'list':
                for _id, name in  [(x, y[0]) for x, y in peripheral_names.items()]:
                    print("{}--{}".format(_id, name))
            else:
                print("Couldn't find peripheral {}.\nHere's a list of peripherals:".format(inp))
                for _id, name in  [(x, y[0]) for x, y in peripheral_names.items()]:
                    print("{}--{}".format(_id, name))
        else:
            inp = input("{}--{}$ ".format(peripheral_in_use, peripheral_names[peripheral_in_use][0]))
            if inp in ('exit', 'quit', 'q'):
                peripheral_in_use = None
            else:
                peripheral_names[peripheral_in_use][1].write(inp)


def update_peripherals(serials):
    peripherals = []
    for serial in serials:
        peripherals.append(recognize_serial(serial))
    peripheral_names = {}
    i = 0
    for peripheral in peripherals:
        peripheral_names.update({i: (peripheral.__class__.__name__, peripheral)})
    return peripheral_names





if __name__ == '__main__':
    main()