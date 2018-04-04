from . import data_parser
from os import path

DATA_FILENAME = path.dirname(__file__) + '/data.conf'
DATA = data_parser.parse(DATA_FILENAME)

# essential functions
# 输入二进制串均用字符串表达，必要时可以在函数内通过bin(str, 2)转为二进制流，但输出前必须转为string
#
# zip_1
#   压缩置换1，位于密钥变换第一步，64bits -> 56bits

def zip_1(M):
    # print ("Input of zip_1: ", M)
    res = ""
    for i in range(0, len(DATA["PC1"])):
        res = res + M[DATA["PC1"][i]-1]
    # print ("Output of zip_1: ", res)
    return (res)

# zip_2:
#   压缩置换2，位于密钥变换输出前，56bits -> 48bits

def zip_2(M):
    # print ("Input of zip_2: ", M)
    res = ""
    for i in range(0, len(DATA["PC2"])):
        res = res + M[DATA["PC2"][i]-1]
    # print ("Output of zip_2: ", res)
    return (res)

# IP:
#   IP置换，加密、解密过程第一步，可逆置换

def IP(M):
    # print ("Input of IP: ", M)
    res = ""
    for i in range(0, len(M)):
        res = res + M[DATA["IP"][i]-1]
    # print ("Output of IP: ", res)
    return (res)
    
# IP_rev:
#   IP置换逆变换

def IP_rev(M):
    # print ("Input of IP_rev: ", M)
    res = ""
    for i in range(0, len(M)):
        res = res + M[DATA["IP_rev"][i]-1]
    # print ("Output of IP_rev: ", res)
    return (res)
    
# left_shift:
#   左移操作

def left_shift(M, i):
    # print ("Input of left_shift: ", M)
    left = M[:int(len(M)/2)]
    right = M[int(len(M)/2):]
    shift = DATA["shift"][i]
    left_new = left[shift:]+left[:shift]
    right_new = right[shift:]+right[:shift]
    res = left_new + right_new
    # print ("Output of left_shift: ", res)
    return (res)

# right_shift:
#   右移操作

def right_shift(M, i):
    # print ("Input of right_shift: ", M)
    left = M[:int(len(M)/2)]
    right = M[int(len(M)/2):]
    shift = len(left)-DATA["shift"][i]
    left_new = left[shift:]+left[:shift]
    right_new = right[shift:]+right[:shift]
    res = left_new + right_new
    # print ("Output of right_shift: ", res)
    return (res)

# right:
#   取右端

def right (M):
    return (M[int(len(M)/2):])

# left:
#   取左端

def left (M):
    return (M[:int(len(M)/2)])

# F:
#   Feistel函数

def F (key, M):
    ext_M = ""
    for i in range(0,len(DATA["Ext"])):
        ext_M = ext_M + M[DATA["Ext"][i]-1]
    # print (len(ext_M))
    mid = xor(ext_M,key)
    # print (ext_M)
    # print (key)
    # print (mid)
    mid2 = ""
    for i in range(1,len(DATA["Sbox"])+1):
        # print (i)
        input = mid[6*(i-1):6*i]
        # print (input)
        ind1 = int(input[0]+input[5],2)
        ind2 = int(input[1:5],2)
        Sbox = DATA["Sbox"][str(i)]
        out = bin(Sbox[ind1][ind2])[2:]
        out = ("0000"+out)[-4:]
        mid2 = mid2 + out
    res = ""
    # print (len(DATA["P"]))
    # print (len(mid2))
    for i in range(0,len(DATA["P"])):
        res = res + mid2[DATA["P"][i]-1]
    return (res)

# xor:
#   异或操作

def xor (a,b):
    l = len(a)
    res = "0000000000000000000000000000000000000000000000000000000000000000" + bin(int(a,2) ^ int(b,2))[2:]
    return (res[-l:])

# join:
#   拼接操作

def join (left, right):
    return (left+right)

# check:
#   位数检验

def check (M,i):
    return (len(M) == i)