#!/usr/bin/python
# -*- coding: UTF-8 -*-

#按行读入文件
f = open("C:\\Users\\thinkpad\\Desktop\\ghi.txt","r")
str = f.readlines()

#遍历查询是否有一行存在两个相同块
for s in str:
    s = s.replace("\n","")
    tmp = []
    tmp = [s[i:i+16] for i in range(0, len(s), 16)]
    #loop作为第二层的循环标志用于在找到相同块后跳出循环
    loop = 1
    for m in range (0, len(s)/16) :
        if(loop == 1):
            for n in range (m+1, len(s)/16):
                #比较两个字符串是否相同
                flag = cmp(tmp[m],tmp[n])
                if (not flag):
                    print s
                    #改变loop用于下一个第二层循环时直接跳出
                    loop = 0
                    break
        else: break