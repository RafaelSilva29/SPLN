#!/usr/bin/env python3
import fileinput
import re

occur = {}

for line in fileinput.input():
    line = line.strip()
    # lista = re.split(r"[,._;\s]+",line)
    # \w (alfa numericos) \W (contrario de alfa numericos)
    lista = re.split(r"\W+",line)
    for w in lista:
        if len(w) > 0:
            occur[w] = occur.get(w,0) + 1

for w,v in sorted(occur.items(),key= lambda x : x[1]):
	print(w,"->",v)