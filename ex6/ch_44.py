# -*- coding: UTF-8 -*-

import hashlib

p = int("800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1",16)
q = int("f4f47f05794b256174bba6e9b396a7707e563c5b",16)
g = int("5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291",16)

right_y = "0x2d026f4bf30195ede3a088da85e398ef869611d0f68f0713d51c9c1a3a26c95105d915e2d8cdf26d056b86b8a7b85519b1c23cc3ecdc6062650462e3063bd179c2a6581519f674a61f1d89a1fff27171ebc1b93d4dc57bceb7ae2430f98a6a4d83d8279ee65d71c1203d2c96d65ebbf7cce9d32971c3de5084cce04a2e147821"
sha1_x = "ca8f6f7c66fa362d40760d135b763eb8527d3d52"

def readTxt(path):
    f  = open(path)
    lines = f.readlines()
    return lines

# 扩展欧几里德算法
def e_gcd(a, b):
    if b == 0:
        return 1, 0, a
    (x, y, r) = e_gcd(b, a % b)
    return y, x - a // b * y, r

# 扩展欧几里德算法求逆，返回a模m的逆
def modinv(a, m):
    x, y, r = e_gcd(a, m)
    if r != 1:
        print '模逆不存在！'
        return -1
    else:
        return x % m

def get_this_k( m1, m2, s1, s2):
    if m1 > m2 :
        Dm = m1 - m2
    else: Dm = m2 - m1 #m1<m2时
    if s1 >s2 :
        Ds = s1 - s2
    else: Ds = s2 -s1  #s1<s2时
    k = (Dm * modinv(Ds, q)) % q
    return k

def get_this_x(this_r, this_s, this_k, H_msg):
    x = (((this_s * this_k) - H_msg) * modinv(this_r , q)) % q
    return x

def get_this_y(x):
    this_y = pow(g , x , p)
    return this_y

def check_this_k(this_k, a):
    this_r = r[a]
    this_s = s[a]
    this_x = get_this_x(this_r, this_s, this_k, m[a])
    this_y = get_this_y(this_x)
    if hex(this_y)[:-1] == right_y:
        print "Find collision! The private key is :", hex(this_x)[2:-1]
        print "- - -Check the private by sha1- - -"
        check_x(hex(this_x)[2:-1])
        return True

def check_x(x):
    if hashlib.sha1(x).hexdigest() == sha1_x:
        print "Yes, the answer is right.\n"

def get_collision():
    for a in range(0,len(m)):
        for b in range(a+1,len(m)):
            this_k = get_this_k(m[a], m[b], s[a], s[b])
            if(check_this_k(this_k, a)):
                return


if __name__ == '__main__':
    path = "C:\\Users\\thinkpad\\Desktop\\info.txt"
    msg = []
    s = []
    r = []
    m = []
    lines = readTxt(path)
    for line in lines:
        if line.startswith("msg:"):
            sha1 = hashlib.sha1(line[5:-1]).hexdigest()
            msg.append(int(sha1,16))
        if line.startswith("s:"):
            s.append(int(line[3:-1]))
        if line.startswith("r:"):
            r.append(int(line[3:-1]))
        if line.startswith("m:"):
            m.append(int(line[3:-1],16))

    get_collision()
