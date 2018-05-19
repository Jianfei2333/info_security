import DES
import random

# 2进制，16进制转换

def _2hex(s):
    return (hex(int(s,2))[2:])

def _2bin(s):
    b = bin(int(s,16))[2:]
    delta = 64 - len(b)%64
    b = "0"*delta + b
    return (b)

# 明文二进制编码，解码

def encode(s):
    return '100000'.join([bin(ord(c)).replace('0b', '') for c in s])

def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split('100000')]])

# IO处理

def read_str(s):
    str = input("请输入"+s+": ")
    return (str)

# 随机密钥生成

def keygen():
    """
    生成随机密钥
    长度：64bit
    有效位数：56
    其中奇偶校验分别为第8*n位
    返回字符串，可以直接输入至加密、解密算法
    """
    flag = False
    key = ""
    for i in range(0,64):
        if ((i+1)%8 == 0):
            if (flag):
                key = key + "1"
            else:
                key = key + "0"
            continue
        r = random.random()>0.5
        # 每出现一个1，flag变化一次
        # 七位里奇数次1时，flag为1
        # 七位里偶数次1时，flag为0
        if (r):
            key = key + "1"
            flag = not flag
        else:
            key = key + "0"
    key_in_bin = bin(int(key, 2))[2:]
    if (len(key_in_bin) != 64):
        delta = 64 - len(key_in_bin)
        key_in_bin = "0"*delta+key_in_bin
    return {"bin": key_in_bin, "hex":_2hex(key_in_bin)}

k = keygen()

# 明文
# c = bin(int('AAAAAFFFFFFFFFFF',16))[2:]

# print ("明文",hex(int(c,2)))
# p = DES.encrypt(c, k)
# print ("密文",hex(int(p,2)))

# c1 = DES.decrypt(p, k)
# print ("明文",hex(int(c1,2)))

# 将字符串编码为二进制串，返回01字符串，进入下一步处理
# 用'100000'表示字符分隔

def cut(s, num):
    b = encode(s)
    # 计算相差位数
    delta = num - len(b)%num
    # print (delta)
    # print (b)
    # 补充差位（用0）
    b = b+("0"*delta)
    # print (b)
    bins = []
    while(len(b) != 0):
        bins.append(b[:num])
        b = b.split(b[:num],1)[1]
    return {"data":bins, "addition_count":delta}

# print (cut(read_str(), 64))

def encryptor():
    # 明文：
    plain = read_str("明文")
    # 生成密钥：
    key = keygen()
    k = key["bin"]
    print ("Your key: ", key["hex"])
    # 编码，裁剪：
    encrypt_package = cut(plain, 64)
    print ("Your additional bits count: ", encrypt_package["addition_count"])
    cipher = ""
    for d in encrypt_package["data"]:
        # print (d)
        cipher += DES.encrypt(d, k, silence=True)
    print (_2hex(cipher))
    print (len(cipher))
    new_plain = ""


def decryptor():
    # 密文：
    cipher = read_str("密文")
    # 补位：
    addition = read_str("补充位数")
    # 密钥：
    k = read_str("密钥")
    # 裁剪：
    decrypt_package = cut(_2bin(cipher), 64)
    plain = ""
    if (decrypt_package['addition_count']!=0):
        print (decrypt_package['addition_count'])
        print ("Error: Bits check failed, maybe the cipher you've input was wrong?")
        # return
    else:
        for d in decrypt_package["data"]:
            plain += DES.decrypt(d, k, silence=True)
    print (decode(plain))



encryptor()
# decryptor()