#!/usr/bin/python
# -*- coding: UTF-8 -*-


#print("hex1 ^ hex2 = %x")%(hex)
#hex1 ^ hex2 = 746865206b696420646f6e277420706c6179

#异或
def myxor (string1 , string2):
    l1 = toHex(string1)
    l2 = toHex(string2)
    l3 = []
    for x in range(0, len(l1)):
        l3.append(hex(int(l1[x], 16) ^ int(l2[x],16)))
    str = "".join(l3).replace("0x","")
    return str

#拆分字符串
def toHex(string):
    #若字符串位数不是偶数则报错
    if not len(string)%2:
        list = []
        list = [string[i:i+2] for i in range (0, len(string), 2)]
    else: print "字符串位数不正确"
    return list

string1 = "1c0111001f010100061a024b53535009181c"
string2 = "686974207468652062756c6c277320657965"
print(myxor(string1, string2))
#输出：746865206b696420646f6e277420706c6179
