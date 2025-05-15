#!/usr/bin/python3
'''Function validUTF8'''


def validUTF8(data):
    '''method that determines if a given data
    set represents a valid UTF-8 encoding'''
    bytes_num = 0
    for byte in data:
        byte = byte & 0xFF
        if bytes_num == 0:
            if (byte >> 5) == 0b110:
                bytes_num = 1
            elif (byte >> 4) == 0b1110:
                bytes_bum = 2
            elif (byte >> 3) == 0b11110:
                bytes-num = 3
            elif (byte >> 7) == 0b0:
                continue
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            bytes_num -= 1
    return bytes_num == 0
