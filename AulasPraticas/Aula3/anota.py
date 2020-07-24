#!/usr/bin/env python3

import fileinput
import re

maius = r'(?:[A-Z]\w+(?:[-\']\w+)*|[A-Z]\.)'
de = r'(?:de|da|dos|das)'

#ent = '(' + maius + '(?: ' + maius + '| ' + de + ' ' + maius + ')*' + ')'

ent = f"({maius}(?: {maius}| {de} {maius})*)"
print(ent)

for line in fileinput.input():
    linha = re.sub(ent, r'{\1}', line)
    print(linha)
