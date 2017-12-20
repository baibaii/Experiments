# -*- coding: UTF-8 -*-

def F_Function(X0, X1, X2, X3, rk):         #轮函数F
    temp = X1 ^ X2 ^ X3 ^ rk
    return X0 ^ T_Function(temp)

def T_Function(x):                          #合成置换T
    T = L_Function(t_Function(x))
    return T

def T_prime_Function(x):                          #合成置换T   #2189675369  0x8283cb69
    T_prime = L_prime_Function(t_Function(x))
    return T_prime

def t_Function(A):                          #非线性变换t   #2189675369  0x8283cb69  dec int
    A = hex(A)[2:-1].zfill(8)
    newA = [A[i:i + 2] for i in xrange(0, len(A), 2)]
    #print "newA:",newA  ['82', '83', 'cb', '69']
    for i in range(0, 4): newA[i] = int(newA[i], 16)
    B = [0]*4
    B[0] = int(Sbox(newA[0]),16)
    B[1] = int(Sbox(newA[1]),16)
    B[2] = int(Sbox(newA[2]),16)
    B[3] = int(Sbox(newA[3]),16)
    #print "B",B
    return B #[] len4 dec int

def L_Function(B):  #L ok
    for i in range(0, 4): B[i] = hex(B[i])[2:].zfill(2)
    B = ''.join(B) #hex str
    B = int(B ,16)
    C = B ^ Rotate(B, 2) ^ Rotate(B, 10) ^ Rotate(B, 18) ^ Rotate(B, 24)
    #print "T =", hex(C)
    return C  #32bits dec int

def L_prime_Function(B): #L' ok
    for i in range(0, 4): B[i] = hex(B[i])[2:].zfill(2)
    B = ''.join(B) #hex str
    B = int(B ,16)
    C = B ^ Rotate(B, 13) ^ Rotate(B, 23)
    #print "T'=", hex(C)
    return C  #32bits dec int

def Reverse(A0, A1, A2, A3):  #ok
    tmp = [A3, A2, A1, A0]
    return tmp

def Rotate(x, n):
    y = ((x >> (32 - n)) + (x << n) & 0xffffffff)
    return y



def Sbox(x):  #ok  Sbox
    table = [
        [0xd6, 0x90, 0xe9, 0xfe, 0xcc, 0xe1, 0x3d, 0xb7, 0x16, 0xb6, 0x14, 0xc2, 0x28, 0xfb, 0x2c, 0x05],
        [0x2b, 0x67, 0x9a, 0x76, 0x2a, 0xbe, 0x04, 0xc3, 0xaa, 0x44, 0x13, 0x26, 0x49, 0x86, 0x06, 0x99],
        [0x9c, 0x42, 0x50, 0xf4, 0x91, 0xef, 0x98, 0x7a, 0x33, 0x54, 0x0b, 0x43, 0xed, 0xcf, 0xac, 0x62],
        [0xe4, 0xb3, 0x1c, 0xa9, 0xc9, 0x08, 0xe8, 0x95, 0x80, 0xdf, 0x94, 0xfa, 0x75, 0x8f, 0x3f, 0xa6],
        [0x47, 0x07, 0xa7, 0xfc, 0xf3, 0x73, 0x17, 0xba, 0x83, 0x59, 0x3c, 0x19, 0xe6, 0x85, 0x4f, 0xa8],
        [0x68, 0x6b, 0x81, 0xb2, 0x71, 0x64, 0xda, 0x8b, 0xf8, 0xeb, 0x0f, 0x4b, 0x70, 0x56, 0x9d, 0x35],
        [0x1e, 0x24, 0x0e, 0x5e, 0x63, 0x58, 0xd1, 0xa2, 0x25, 0x22, 0x7c, 0x3b, 0x01, 0x21, 0x78, 0x87],
        [0xd4, 0x00, 0x46, 0x57, 0x9f, 0xd3, 0x27, 0x52, 0x4c, 0x36, 0x02, 0xe7, 0xa0, 0xc4, 0xc8, 0x9e],
        [0xea, 0xbf, 0x8a, 0xd2, 0x40, 0xc7, 0x38, 0xb5, 0xa3, 0xf7, 0xf2, 0xce, 0xf9, 0x61, 0x15, 0xa1],
        [0xe0, 0xae, 0x5d, 0xa4, 0x9b, 0x34, 0x1a, 0x55, 0xad, 0x93, 0x32, 0x30, 0xf5, 0x8c, 0xb1, 0xe3],
        [0x1d, 0xf6, 0xe2, 0x2e, 0x82, 0x66, 0xca, 0x60, 0xc0, 0x29, 0x23, 0xab, 0x0d, 0x53, 0x4e, 0x6f],
        [0xd5, 0xdb, 0x37, 0x45, 0xde, 0xfd, 0x8e, 0x2f, 0x03, 0xff, 0x6a, 0x72, 0x6d, 0x6c, 0x5b, 0x51],
        [0x8d, 0x1b, 0xaf, 0x92, 0xbb, 0xdd, 0xbc, 0x7f, 0x11, 0xd9, 0x5c, 0x41, 0x1f, 0x10, 0x5a, 0xd8],
        [0x0a, 0xc1, 0x31, 0x88, 0xa5, 0xcd, 0x7b, 0xbd, 0x2d, 0x74, 0xd0, 0x12, 0xb8, 0xe5, 0xb4, 0xb0],
        [0x89, 0x69, 0x97, 0x4a, 0x0c, 0x96, 0x77, 0x7e, 0x65, 0xb9, 0xf1, 0x09, 0xc5, 0x6e, 0xc6, 0x84],
        [0x18, 0xf0, 0x7d, 0xec, 0x3a, 0xdc, 0x4d, 0x20, 0x79, 0xee, 0x5f, 0x3e, 0xd7, 0xcb, 0x39, 0x48]]

    r = x / 16
    l = x % 16
    return hex(table[r][l])[2:]

def rkGenerate(MK0, MK1, MK2, MK3):   #ok 密钥扩展算法 hex str
    FK0 = 0xA3B1BAC6
    FK1 = 0x56AA3350
    FK2 = 0x677D9197
    FK3 = 0xB27022DC

    #dec int
    MK0 = int(MK0, 16)
    MK1 = int(MK1, 16)

    MK2 = int(MK2, 16)
    MK3 = int(MK3, 16)

    #32bits
    K0 = MK0 ^FK0
    K1 = MK1 ^ FK1
    K2 = MK2 ^ FK2
    K3 = MK3 ^ FK3

    #print K0,K1,K2,K3
    #2727542689 3741449919 2577476367 3290697932

    CK = [0x00070e15, 0x1c232a31, 0x383f464d, 0x545b6269,
          0x70777e85, 0x8c939aa1, 0xa8afb6bd, 0xc4cbd2d9,
          0xe0e7eef5, 0xfc030a11, 0x181f262d, 0x343b4249,
          0x50575e65, 0x6c737a81, 0x888f969d, 0xa4abb2b9,
          0xc0c7ced5, 0xdce3eaf1, 0xf8ff060d, 0x141b2229,
          0x30373e45, 0x4c535a61, 0x686f767d, 0x848b9299,
          0xa0a7aeb5, 0xbcc3cad1, 0xd8dfe6ed, 0xf4fb0209,
          0x10171e25, 0x2c333a41, 0x484f565d, 0x646b7279 ]

    K = [0] * 36
    K[0] = K0
    K[1] = K1
    K[2] = K2
    K[3] = K3

    rk = []
    for i in range(0, 32, 1):
        #T_prime_para = K[i+1] ^ K[i+2] ^ K[i+3] ^ CK[i]
        #print T_prime_para
        #2189675369  0x8283cb69
        newK = K[i] ^ T_prime_Function(K[i+1] ^ K[i+2] ^ K[i+3] ^ CK[i])  #K[i+4]
        K[i+4] = newK
        #CKi = hex(CK[i])[2:]
        #newCKi = [CKi[i:i + 2] for i in xrange(0, len(CKi), 2)]

        #print "k", i+1, hex(K[i+1]), " k", i+2, hex(K[i+2]), " k", i+3, hex(K[i+3]), hex(CK[i])
        #print "K[i+1] ^ K[i+2] ^ K[i+3] ^ CK[i]:", hex(K[i + 1] ^ K[i + 2] ^ K[i + 3] ^ CK[i])
        print "rk[", i,"] = ", hex(newK)[:-1]
        rk.append(newK)
    return rk

def Encrypt(X0, X1, X2, X3, rk):  # ok
    X0 = int(X0, 16)
    X1 = int(X1, 16)
    X2 = int(X2, 16)
    X3 = int(X3, 16)

    X = [0] * 36
    X[0] = X0
    X[1] = X1
    X[2] = X2
    X[3] = X3

    i = 0
    while (i < 32):
        this_rk = rk[i]
        newX = F_Function(X[0 + i], X[1 + i], X[2 + i], X[3 + i], this_rk)  # X[i+4]
        #X.append(newX)
        X[i+4] = newX
        #print "newX", hex(newX)
        print "X[",i,"]=",hex(newX)[:-1]
        i = i + 1
    Y = Reverse(X[32], X[33], X[34], X[35])
    for i in range(0, 4, 1):
        Y[i] = hex(Y[i])[2:-1].zfill(8)
    return ''.join(Y)

if __name__ == '__main__':

    plaintext = "0123456789abcdeffedcba9876543210"
    newplaintext = [plaintext[i:i + 8] for i in xrange(0, len(plaintext), 8)]
    print newplaintext  #['01234567', '89abcdef', 'fedcba98', '76543210']

    key = "0123456789abcdeffedcba9876543210"
    newkey = [key[i:i + 8] for i in xrange(0, len(key), 8)]
    print newkey  #['01234567', '89abcdef', 'fedcba98', '76543210']

    rk = rkGenerate(newkey[0], newkey[1], newkey[2], newkey[3])
    #print rk
    #print len(rk)
    Y = Encrypt(newplaintext[0], newplaintext[1], newplaintext[2], newplaintext[3], rk)
    print Y
    count = 0