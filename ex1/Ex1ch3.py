#!/usr/bin/python
# -*- coding: UTF-8 -*-

#字符串两两分组存入列表
str1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
str = []
str = [str1[i:i + 2] for i in xrange(0, len(str1), 2)]

#统计词频
feq = {}
for x in str:
    if str.count(x)>1:
        feq[x] = str.count(x)
s1 = max(feq, key=feq.get)
#s1 = 78

#统计结果显示0x78出现次数最多，对应空格，异或之后得到密钥
key = chr(int(s1, 16) ^ 0x20)
print("key = %s")%(key)
#key = X

#key与密文异或得到明文
text = []
for x in str:
    text.append(chr(ord(key) ^ int(x,16)))
print ''.join(text)
#Cooking MC's like a pound of bacon
