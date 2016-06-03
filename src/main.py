import ports_listener
from serial_recognizer import recognize_serial


def main():
    print("Waiting for peripherals to connect...")
    threads, serials, stop_event = ports_listener.loop_start_listening()
    peripherals = []
    for serial in serials:
        peripherals.append(recognize_serial(serial))

    peripheral_in_use = None
    peripheral_names = {}
    i = 0
    for peripheral in peripherals:
        peripheral_names.update({i: (peripheral[0].__class__.__name__, peripheral[0])})

    while True:
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
                print("Couldn't find peripheral {}".format(inp))
        else:
            inp = input("{}--{}$ ".format(peripheral_in_use, peripheral_names[peripheral_in_use][0]))
            if inp in ('exit', 'quit', 'q'):
                peripheral_in_use = None
            else:
                peripheral_names[peripheral_in_use][1].write(inp)





if __name__ == '__main__':
    main()