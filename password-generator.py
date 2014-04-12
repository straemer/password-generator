#!/usr/bin/python3

import sys
import os
import struct

#taken from http://stackoverflow.com/a/14720865
_random_source = open("/dev/random", "rb")

def random_bytes(len):
    return _random_source.read(len)

def unpack_uint32(bytes):
    tup = struct.unpack("I", bytes)
    return tup[0]

UINT32_MAX = 0xffffffff
def randint(low, high):
    """
    Return a random integer in the range [low, high], including
    both endpoints.
    """
    n = (high - low) + 1
    assert n >= 1
    scale_factor = n / float(UINT32_MAX + 1)
    random_uint32 = unpack_uint32(random_bytes(4))
    result = int(scale_factor * random_uint32) + low
    return result

allChars = '`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'

length = int(sys.argv[1])

password = ''

for i in range(length):
    password += allChars[randint(0,len(allChars))]

print(password)
