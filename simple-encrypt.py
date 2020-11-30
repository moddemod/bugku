#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： moddemod
# datetime： 2019/12/26 上午11:01 
# ide： PyCharm

import base64
# 栅栏key为4
s = 'e6Z9i~]8R~U~QHE{RnY{QXg~QnQ{^XVlRXlp^XI5Q6Q6SKY8jUAA'
print(ord('='))
print(ord('A'))
s1 = ''
for i in s:
    s1 += chr(ord(i) - 4)
print(s1)

# base64解密
s2 = base64.b64decode(s1)
s2 = s2.decode()
print(s2)
