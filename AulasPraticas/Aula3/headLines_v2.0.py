#!/usr/bin/env python3
import fileinput
import re
import sys

for line in fileinput.input():
    if fileinput.filelineno() > 10:
        fileinput.nextfile()
    if fileinput.isfirstline():
        print(f'==> { fileinput.filename() } <=== ') 

