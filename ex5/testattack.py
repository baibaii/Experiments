# -*- coding: UTF-8 -*-

import os
import gmpy2
import subprocess
import math

def readFiles(path):
    #path = "D:/Python34/news" #文件夹目录  
    files= os.listdir(path) #得到文件夹下的所有文件名称  
    s = []
    i = 0
    for file in files:#遍历文件夹  
        if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开  
            f = open(path+"/"+file);#打开文件
            iter_f = iter(f);#创建迭代器
            tmp = []
            str = ""
            for line in iter_f:
                str = str + line
            tmp.append(str)
            #print(tmp)
            s.append(tmp)#每个文件的文本存到list中  
    #print(s)#打印结果 
    return s

# 读入文件
def readEachFile():
    file_address = open(r'C:\Users\thinkpad\Desktop\getRSA\Frame9')
    try:
        file_context = file_address.read()
    finally:
        file_address.close()
    # print(type(file_context))
    str_text = [file_context[i:i + 256] for i in range(0, len(file_context), 256)]
    #print(str_text)
    hex_text = []
    for x in str_text:
        hex_text.append(int(x, 16))
        #print(int(x, 16))

#对传入的列表进行分割并转为十进制，返回具有三个元素的列表
def eachPartition(file_context):
    str_text = [file_context[i:i + 256] for i in range(0, len(file_context), 256)]
    #print(str_text)
    dec_text = []
    for x in str_text:
        #print(type(x))str
        dec_text.append(int(x, 16))
        #print(int(x, 16))
    return dec_text

#将s中每个列表分割并转为十进制
def partition(s):
    dec_text = []
    for list in s:
        for file_context in list:
            dec_text.append(eachPartition(file_context))
    return dec_text

#求最大公约数
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


# 扩展欧几里德算法
def e_gcd(a, b):
    if b == 0:
        return 1, 0, a
    (x, y, r) = e_gcd(b, a % b)
    return y, x - a // b * y, r

# 扩展欧几里德算法求逆
def modinv(a, m):
    x, y, r = e_gcd(a, m)
    if r != 1:
        print '模逆不存在！'
        return -1
    else:
        return x % m

# 共模攻击
def attackSameModule(e1, e2, c1, c2, N):
    (s1, s2, r) = e_gcd(e1, e2)
    if r == 1:
        return (pow(c1, s1) * pow(c2, s2)) % N
    else: print "e不互质！"

#针对具有公因数的两个帧的攻击
def attackGcd(i, m):
    thisgcd = gcd(s1[i][0], s1[m][0])
    ip = thisgcd
    s1[i].append(ip)
    iq = s1[i][0] / ip
    s1[i].append(iq)
    ifin = (ip - 1) * (iq - 1)
    s1[i].append(ifin)
    #s1[i]=[n,e,c,p,q,fin]

    mp = thisgcd
    s1[m].append(mp)
    mq = s1[m][0] / mp
    s1[m].append(mq)
    mfin = (mp - 1) * (mq - 1)
    s1[m].append(mfin)

    return getPlaintextM(s1[i][0], s1[i][1], s1[i][2], s1[i][3], s1[i][4]), getPlaintextM(s1[m][0], s1[m][1], s1[m][2], s1[m][3], s1[m][4])

#获取明文文本
def getPlaintextM(n, e, c, p, q):
    d = modinv(e, (p - 1) * (q - 1))
    if d == -1:
        print "failed to get the modinv"
        return -1
    else:
        m = hex(pow(c, d, n))   #经过填充的明文
        return getASCII(m)

#得到有效的明文信息并进行ascii变换返回明文文本
def getASCII(m):
    a = m[-17: -1]
    plaintext = ''.join([chr(int(b, 16)) for b in [a[i:i + 2] for i in range(0, len(a), 2)]])
    return plaintext

#低加密指数攻击
def attackLittleE(N, e, c):
    k = 0
    while 1:
        m = gmpy2.iroot(c+k*N, e)
        if(m[1] == True):
            return m
        if(k == 100000000):break
        k = k+1

# 广播攻击
def attackwith_Boardcast(Cs, Ns, e):
    N = 1
    for n in Ns:
        N *= n
    result = 0
    for a, n in zip(Cs, Ns):
        m = N / n
        r, s, d = e_gcd(n, m)
        if d != 1:
            return -2
            #raise "Input not pairwise co-prime"
        result += a * s * m
    x, n = result % N, N
    realnum = gmpy2.iroot(gmpy2.mpz(x), e)[0].digits()
    return  realnum

def todo_broadcast(Cs, Ns, e):
    cs = []
    ns = []
    for i in range(0, len(Cs), 1):
        for m in range(i + 1, len(Cs), 1):
            cs = (Cs[i:m+1])
            ns = (Ns[i:m+1])
            plaintext = attackwith_Boardcast(cs, ns, e)
            if plaintext > 0:
                #print hex(int(plaintext))
                conduct_broadcast(e, hex(int(plaintext)))
            else:
                print "failed e" + str(e) + "!"

def conduct_broadcast(e, maybe_plaintext):
    if len(maybe_plaintext) == 131:
        print "Get the plaintext of e = ", e, maybe_plaintext
        print "The specific ASCII is :\n",getASCII(maybe_plaintext) #t is a f

# 费马分解法
def attackByFermat(N):
    k = int(math.sqrt(N)) + 1
    y = k * k - N
    d = 1
    y_2 = math.sqrt(y)
    while(bool((math.ceil(math.sqrt(y))) != (math.sqrt(y))) & bool((math.ceil(math.sqrt(y))) >= N/2 )):
        y = y + 2 * k +d
        d = d + 2
        if(math.sqrt(y) < 0): break
    if(int(math.sqrt(y)) < N/2):
        print "- - - Fermat failed - - - !No factor! "
    else:
        x = math.sqrt(N + y)
        y = math.sqrt(y)
        p = x - y
        q = math.sqrt(x + y)
        print "- - - Fermat succeeded - - -\n", "p:\n", p, "\nq:\n", q


def Fermat(i, N):
    x = long(math.sqrt(N));
    if x * x < N:
        x += 1;
     # y^2 = x^2 - num
    while (1):
        y2 = x * x - N;
        y = 0
        if y2 > 0: y = long(math.sqrt(y2))
        if y * y == y2:
            break
        if y * y > N ** (1/4):
            print "failed!",i
            break
            return -1
        x += 1;
    if ((x+y)!=(x-y)): print "- - - Fermat - - -[", i, "]\n", "p:\n", hex(x+y), "\nq:\n", hex(x-y)
    return [x + y, x - y];

def attackPollard(N, B):
    a = 2
    k = 1
    while(k<=B):
        a = (a ** k) % N
        p = gcd(a-1, N)
        if (1<p<N):
            q = N/p
            print "- - - Pollard succeeded - - -\n", "p:\n", hex(p), "\nq:\n",hex(q)
            break
        k = k+1


#特征检测
def check(s1):
    Cs3 =[]
    Ns3 = []
    Cs5 = []
    Ns5 = []
    for i in range(0, len(s1), 1):
        #print "i=" +str(i)
        #Fermat(i, s1[i][0])
        attackPollard(s1[i][0], 1024)
        for m in range(i+1, len(s1), 1):
            if s1[i][0] == s1[m][0]:
                print "- - - N相同 - - -"
                print "第"+ str(i) +"组与第"+ str(m) +"组N相同,具体为\n"+ str(s1[i][0]) + "\n可尝试共模攻击"
                #m = attackSameModule(s1[i][1], s1[m][1], s1[i][2], s1[m][2], s1[i][0])
                #print "明文为" + str(m)
                print "\n"
            elif type(gcd(s1[i][0], s1[m][0])) == type(s1[m][0]) and gcd(s1[i][0], s1[m][0])!=1:
                print "- - - 有公约数 - - -"
                print "第"+ str(i) +"组与第"+ str(m) +"组的N有公约数,公约数为\n"+ str(gcd(s1[i][0], s1[m][0]))
                plaintexti, plaintextm = attackGcd(i, m)
                print "第"+ str(i) +"组的明文为\n" ,plaintexti    #第一组明文：. Imagin
                print "第" + str(m) + "组的明文为\n" ,plaintextm  #第十组明文：m A to B
                print "\n"

            #print "m=" + str(m)
        if s1[i][1] > 65537 :
            print "- - - 加密指数e很大 - - -"
            print "第" + str(i) + "组可尝试低解密指数攻击,e为：\n" + str(s1[i][1])
            print "\n"

        if s1[i][1] <65537 :
            print "第" + str(i) + "组可尝试低加密指数攻击，e为：" + str(s1[i][1])
            #plaintext = attackLittleE(s1[i][0], s1[i][1], s1[i][2])
            #print plaintext
            if s1[i][1] == 3:
                Cs3.append(s1[i][2])
                Ns3.append(s1[i][0])

            if s1[i][1] == 5:
                Cs5.append(s1[i][2])
                Ns5.append(s1[i][0])

    todo_broadcast(Cs3, Ns3, 3) # failed
    todo_broadcast(Cs5, Ns5, 5) # t is a f





if __name__ == '__main__':
    path = "C:\\Users\\thinkpad\\Desktop\\getRSA"
    s = readFiles(path)#s=[[],[],[],[],[]...] s.len = 21
    s1 = partition(s)
    print(s)
    check(s1)