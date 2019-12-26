#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： moddemod
# datetime： 2019/12/25 下午10:13 
# ide： PyCharm

import base64
from html import unescape
import urllib.parse as urlparse

with open('1.txt', 'r') as f:
    r = f.read()
    r1 = base64.b64decode(r)
    print(r1)
    r1 = r1.decode()
    r2 = r1.split('\\')
    print(r2)
    del r2[0]
    print(r2)
    r3 = []
    for i in r2:
        r3.append(chr(int(i, 8)))
    r3 = ''.join(r3)
    print(r3)

    r4 = r3.split('\\x')
    print(r4)
    del r4[0]
    print(r4)
    r5 = []
    for i in r4:
        r5.append(chr(int(i, 16)))
    print(r5)
    r5 = ''.join(r5)
    print(r5)
    # print(type(r5))
    r5 = r5.encode().decode('unicode-escape')
    print(r5)
    r6 = r5.split(',')
    print(r6)
    r6[0] = '38'
    r6[-1] = '59'
    print(r6)
    r7 = []
    for i in r6:
        r7.append(chr(int(i)))
    print(r7)
    r7 = ''.join(r7)
    print(r7)
    r8 = unescape(r7)
    print(r8)
    r9 = unescape(r8)
    print(r9)
    r10 = urlparse.unquote(r9)
    print(r10)
