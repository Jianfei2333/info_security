# DES 出口
# 二进制数据以01字符串形式传递 
from . import util

def encrypt (C, K, silence = False):
    M = C
    T = K
    # print (T, K)
    # Initial handle
    # print (util.check(C,64))
    # print (util.check(K,64))
    if (not util.check(C,64) or not util.check(K,64)):
        print ('Error: Input and Key must be 64 bits.')
    T = util.zip_1(T)
    M = util.IP(M)
    for i in range(0,16):
        T = util.left_shift(T, i)
        Key_to_use = util.zip_2(T)
        L_new = util.right(M)
        E = util.F(Key_to_use, L_new)
        R_new = util.xor(util.left(M), E)
        M = util.join(L_new, R_new)
        if (silence == False):
            print ('round ',i,': ',hex(int(M,2)))
    res = util.IP_rev(M)
    # print (res)
    return (res)

def decrypt (P, K, silence):
    M = P
    T = K
    if (not util.check(P,64) or not util.check(K,64)):
        print ('Error: Input and Key must be 64 bits.')
    T = util.zip_1(T)
    M = util.IP(M)
    for i in range(0,16):
        Key_to_use = util.zip_2(T)
        T = util.right_shift(T, 15-i)
        R_ori = util.left(M)
        E = util.F(Key_to_use, R_ori)
        L_ori = util.xor(util.right(M), E)
        M = util.join(L_ori, R_ori)
        if (silence == False):
            print ('round ',i,': ',hex(int(M,2)))
    res = util.IP_rev(M)
    # print (res)
    return (util.IP_rev(M))