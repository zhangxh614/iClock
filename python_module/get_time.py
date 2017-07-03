import time


def get_time():
    '''return tuple(hour,minute)'''
    return time.localtime()[3:5]


print(get_time())