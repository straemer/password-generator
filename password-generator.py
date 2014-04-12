#!/usr/bin/python3

import sys
import random

allChars = '`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'

length = int(sys.argv[1])

password = ''

for i in range(length):
    password += random.choice(allChars)

print(password)
