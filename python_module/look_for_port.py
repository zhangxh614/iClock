#!/usr/bin/ python
# -*- coding: utf-8 -*

import serial
import serial.tools.list_ports


def get_ser_name():
    port_list = list(serial.tools.list_ports.comports())

    if len(port_list) <= 0:
        return None

    else:
        port_list_0 = list(port_list[0])

        port_serial = port_list_0[0]

        ser = serial.Serial(port_serial, 9600, timeout=60)

        return ser.name


print(get_ser_name())