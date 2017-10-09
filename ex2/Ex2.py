#!/usr/bin/python
# -*- coding: UTF-8 -*-

from oracle import *
import sys

if len(sys.argv) < 2:
    print "Usage: python sample.py <filename>"
    sys.exit(-1)

f = open(sys.argv[1])
data = f.read()
f.close()
#data = "9F0B13944841A832B2421B9EAF6D9836813EC9D944A5C8347A7CA69AA34D8DC0DF70E343C4000A2AE35874CE75E64C31"

ctext = [(int(data[i:i+2],16)) for i in range(0, len(data), 2)]
C = [ctext[:16], ctext[16:32], ctext[-16:]]

P = [[0] * 16, [0] * 16]                        #存储明文
MidValue = [[0] * 16, [0] * 16]         #存储中间值

Oracle_Connect()
for bi in range(2):                 #给出的密文仅可分成3块，故只需要计算两次
    b = 2 - bi                      #猜解出的值为倒序存入列表，方便起见设置b变量
    C1 = [C[b - 1][:], C[b][:]]  # C1存储将要提交给服务器的值，从C列表中复制需要的密文块
    for i in range(16):  #改变不参与遍历的字节，全部置零
        C1[0][i] = 0
    for k in range(16):
        pos = 15 - k
        ii = -1
        for i in range(256):
            C1[0][pos] = i
            rc = Oracle_Send(C1[0][:] + C1[1][:], 2)    #猜测的密文块发给服务器判断，若符合填充标准则返回1
            #print rc
            if rc == 1:                                 #若返回1，则可求出中间值与对应的明文
                ii = i
                break
        MidValue[b-1][pos] = ii ^ (k + 1)
        P[b-1][pos] = C[b-1][pos] ^ MidValue[b-1][pos]

        for i in range(pos , 16):                       # 修正已得到的中间值，即已猜解出的中间值的字节分别与正在padding的序列长度异或
            C1[0][i] = (k + 2) ^ MidValue[b-1][i]
Oracle_Disconnect()

#P[0] = [89, 97, 121, 33, 32, 89, 111, 117, 32, 103, 101, 116, 32, 97, 110, 32]
#P[1] = [65, 46, 32, 61, 41, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
text = []
for x in P[0]:
    text.append(chr(x))
for x in P[1]:
    if(x == 11):
        break
    else:
        text.append(chr(x))
a = ""
print ("the text is: %s") % a.join(text)
#the text is:Yay! You get an A. =) 
