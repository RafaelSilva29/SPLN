#!/usr/bin/env python3
import fileinput
import re

occur = {}

for line in fileinput.input():
    lista = re.findall(r"\w",line)

    for w in lista:
        occur[w] = occur.get(w,0) + 1

for w,v in sorted(occur.items(),key= lambda x : x[1]):
	print(w,"->",v)