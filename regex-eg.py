#!/usr/bin/env python3.7

import re

p = re.compile('^.+\.conf|^.+\_config')
m = p.match('sshd_config')

#print(m)
file_match = (m.group())
print(file_match)

