import ports_listener
from serial_recognizer import recognize_serial


def main():
    threads, serials, stop_event = ports_listener.start_listening()
    print("Waiting for peripherals to connect...")
    while True:
        if len(serials) > 0:
            break
    peripherals = []
    for serial in serials:
        peripherals.append(recognize_serial(serial))

    peripheral_in_use = None
    peripheral_names = {}
    i = 0
    for peripheral in peripherals:
        peripheral_names.update({i: (peripheral.__class__.__name__, peripheral)})

    while True:
        if peripheral_in_use is None:
            inp = input("Please choose a peripheral to work with ('list'): ")
            if inp in ('exit', 'quit', 'q'):
                break
            elif inp in [x[0] for x in peripheral_names.values()]:
                for item in peripheral_names.items():
                    if item[1][0] == inp:
                        peripheral_in_use = item[0]
            elif inp == 'list':
                for name in [x[0] for x in peripheral_names.values()]:
                    print(name)
            else:
                print("Couldn't find peripheral {}".format(inp))
        else:
            inp = input("{}$ ".format(peripheral_names[peripheral_in_use][0]))
            if inp in ('exit', 'quit', 'q'):
                peripheral_in_use = None
            else:
                peripheral_names[peripheral_in_use][1].write(inp)





if __name__ == '__main__':
    main()