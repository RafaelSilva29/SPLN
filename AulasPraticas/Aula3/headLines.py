#!/usr/bin/env python3
import fileinput
import re
import sys

argc = 0

for arg in sys.argv:
    if argc >= 1:
        i = 0
        print('-------------------- Ficheiro ' + str(arg) + ' --------------------')
        file = fileinput.input(arg)
        for line in file:
            line = line.strip()
            if i<10:
                print(line)
            else:
                break
            i +=1
        file.nextfile()
        print('-----------------------------------------------------------------------')
    argc += 1    

