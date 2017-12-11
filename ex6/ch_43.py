# -*- coding: UTF-8 -*-

import hashlib


p = int("800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1",16)
q = int("f4f47f05794b256174bba6e9b396a7707e563c5b",16)
g = int("5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291",16)
H_msg = int("d2d0714f014a9784047eaeccf956520045c45265",16)
r = 548099063082341131477253921760299949438196259240
s = 857042759984254168557880549501802188789837994940
right_y = "0x84ad4719d044495496a3201c8ff484feb45b962e7302e56a392aee4abab3e4bdebf2955b4736012f21a08084056b19bcd7fee56048e004e44984e2f411788efdc837a0d2e5abb7b555039fd243ac01f0fb2ed1dec568280ce678e931868d23eb095fde9d3779191b8c0299d6e07bbb283e6633451e535c45513b2d33c99ea17"
sha1_x = "0954edd5e0afe5542a4adf012611a91912a3ec16"

def get_this_y(x):
    this_y = pow(g , x , p)
    return this_y

def get_this_x(k):
    x = (((s * k) - H_msg) * modinv(r , q)) % q
    return x

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

def get_this_r(k):
    r = pow(g , k, p) % q
    return r

def get_this_s(k, this_r, x):
    s = (modinv(k , q) * (H_msg + x * this_r)) % q
    return s

def guess_k():
    for k in range(1 , 2**16):
        x = get_this_x(k)
        y = get_this_y(x)
        this_r = get_this_r(k)
        this_s = get_this_s(k, this_r, x)

        if this_r == r :
            if this_s == s:
                print "Get the private key by checking r! It's : ", hex(x)[2:-1]
                print "- - -Check the answer- - -"
                check_x(hex(x)[2:-1])
            #break

        if hex(y)[:-1] == right_y:
            print "Get the private key by checking y! It's :", hex(x)[2:-1]
            print "- - -Check the answer- - -"
            check_x(hex(x)[2:-1])
            break

def check_x(x):
    if hashlib.sha1(x).hexdigest() == sha1_x:
        print "Yes, the answer is right.\n"

if __name__ == '__main__':
    guess_k()