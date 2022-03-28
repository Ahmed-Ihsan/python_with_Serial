import bluetooth

def scan():

    print("Scanning for bluetooth devices:")

    devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True)

    number_of_devices = len(devices)

    print(number_of_devices,"devices found")

    for addr, name, device_class in devices:

        print("\n")

        print("Device:")

        print("Device Name: %s" % (name))

        print("Device MAC Address: %s" % (addr))

        print("Device Class: %s" % (device_class))

        print("\n")

    return devices

devices = scan()
def adress_hc05(devices):
    for i in devices:
        if i[1] == 'HC-05':
            return i
        
HC_05 = adress_hc05(devices)
print(HC_05)
