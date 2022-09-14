#!/usr/bin/env python3

import usb.core
import usb.util
import fcntl
import os

# Thanks to https://github.com/Paufurtado/usbreset.py
USBDEVFS_RESET = ord('U') << (4*2) | 20

if __name__ == "__main__": 

    index = 0
    idVendor = 0x1915
    idProduct = 0x0102

    device = list(usb.core.find(idVendor=idVendor, idProduct=idProduct, find_all=True))[index]
    bus = str(device.bus).zfill(3)
    addr = str(device.address).zfill(3)
    dev_path = "/dev/bus/usb/%s/%s" % (bus, addr)
    fd = os.open(dev_path, os.O_WRONLY)
    try:
        fcntl.ioctl(fd, USBDEVFS_RESET, 0)
    except IOError:
        print("Unable to reset device %s" % filename)
    finally:
        os.close(fd)
