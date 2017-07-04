#!/usr/bin python3
from get_time import get_time
from look_for_port import get_ser
from read_imap_number import get_unseen_number
import time

now_time = [0, 0]
pre_time = [0, 0]
is_mail = 2


def trans2(i):
    if i < 10:
        return '0%d' % i
    else:
        return '%d' % i


if __name__ == '__main__':
    time.sleep(1)
    ser = get_ser()

    while True:
        now_time = get_time()  # (hour, minute)
        unseen_num = get_unseen_number()
        if (unseen_num is None):
            is_mail = 0
        elif (unseen_num == 0):
            is_mail = 2
        else:
            is_mail = 1
        if ser is None:
            print('There is no available bluetooth')
            continue
        message = (trans2(now_time[0]) + trans2(now_time[1]) + '%d' % is_mail)

        time.sleep(4)
        ser.write(bytes(message, 'UTF-8'))
        pre_time = now_time
