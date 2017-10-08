#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

str1 = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
key = "ICE"
text = []
str2 = []
str2 = [str1[i:i + 3] for i in range(0, len(str1), 3)]
for str in str2:
    k = [key[i:i + 1] for i in range(0, len(key), 1)]
        #对应元素一一异或，并存入text中
    for x,y in zip(str,k):
        #去0x补零
        text.append(((hex(ord(x) ^ ord(y))).replace("0x","")).zfill(2))
print  ("%s") % ("".join(text))



