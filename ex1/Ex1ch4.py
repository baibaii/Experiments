#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

#按行读入文件并保存到列str1
f = open("C:\\Users\\thinkpad\\Desktop\\abc.txt", "r")
str1 = f.readlines()

for s in str1[0:len(str1)-1]:
    #去掉每一行的换行符“\n”
    s = s.replace("\n","")
    str2 = []
    str2 = [s[i:i + 2] for i in range(0, len(s), 2)]
    # 统计词频
    feq = {}
    for x in str2:
        if str2.count(x) > 0:
            feq[x] = str2.count(x)
    key = chr(int(max(feq, key=feq.get), 16) ^ 0x20)

    # key与密文异或得到明文
    text = []
    for x in str2:
        text.append(chr(ord(key) ^ int(x, 16)))

    tmp = "".join(text)
    #正则匹配判断可读性
    flag = bool(re.search('^[a-zA-Z0-9\s.]+$', tmp))
    if(flag):
        print tmp





