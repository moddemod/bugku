#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： moddemod
# datetime： 2019/12/25 下午9:54 
# ide： PyCharm

import binascii
import base64
s = '636A56355279427363446C4A49454A7154534230526D684356445A31614342354E326C4B4946467A5769426961453067'
r = binascii.unhexlify(s)
print(r)
r1 = base64.b64decode(r)
print(r1)


# b'cjV5RyBscDlJIEJqTSB0RmhCVDZ1aCB5N2lKIFFzWiBiaE0g'
# b'r5yG lp9I BjM tFhBT6uh y7iJ QsZ bhM '
