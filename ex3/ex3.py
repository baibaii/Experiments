#!/usr/bin/python
# -*- coding: UTF-8 -*-

import hashlib
import time
import itertools

time_start = time.time()        #用于计时
ciphertext = "67ae1a64661ac8b4494666f58c4822408dd0a3e4"
Dic = [["Q", "q"], ["W", "w"], ["5", "%"], ["(", "8"], ["I", "i"], ["=", "0"], ["N", "n"], ["*", "+"]]
count = [0]*8

def guess():
    x = 2
    for x in range(256):
        a = []
        b = 0
        while(x>=1):
            count[b] = x % 2
            x = x/2
            b = b+1
        for x,y in zip(count,range(8)):
            a.append(Dic[y][x])
        #print ''.join(a)
        Texts = list(itertools.permutations(a, 8))
        for x in Texts:
            text = ''.join(x)
            if (hashlib.sha1(text).hexdigest() == ciphertext):   #判断每个字符串的sha1值，须用十六进制表示
                return text

text = guess()
time_end =time.time()
print text
print time_end-time_start,"s"