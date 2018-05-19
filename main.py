import DES
import random

# 2进制，16进制转换

def _2hex(s):
    return (hex(int(s,2))[2:])

def _2bin(s):
    b = bin(int(s,16))[2:]
    delta = 0
    if (len(b)%64 != 0):
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
    # 生成随机密钥
    # 长度：64bit
    # 有效位数：56
    # 其中奇偶校验分别为第8*n位
    # 返回字符串，可以直接输入至加密、解密算法
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

def cut(b, num):
    # b = encode(s)
    # 计算相差位数
    delta = 0
    if len(b)%num != 0:
        delta = num - len(b)%num
    # 补充差位（用0）
    b = b+("0"*delta)
    bins = []
    while(len(b) != 0):
        bins.append(b[:num])
        b = b.split(b[:num],1)[1]
    return {"data":bins, "addition_count":delta}

def encryptor():
    # 明文：
    plain = read_str("明文")
    # 生成密钥：
    key = keygen()
    k = key["bin"]
    print ("Your key: ", key["hex"])
    # 编码:
    b = encode(plain)
    print ('encoding: ', b)
    # 裁剪:
    encrypt_package = cut(b, 64)
    print ("Your additional bits count: ", encrypt_package["addition_count"])
    cipher = ""
    for d in encrypt_package["data"]:
        node = DES.encrypt(d, k, silence=True)
        cipher += node
    print ('密文: '+_2hex(cipher))

    print ('复制以下内容以解密：')
    print (_2hex(cipher)+' '+str(encrypt_package["addition_count"])+' '+key["hex"])


def decryptor():
    everything = read_str('密文，补充位数，密钥，用空格间隔')
    cipher = everything.split(' ')[0]
    addition = everything.split(' ')[1]
    key = everything.split(' ')[2]
    # 密文 cipher
    # 补充位数 addition
    # 密钥 key
    k = _2bin(key)
    # 裁剪：
    decrypt_package = cut(_2bin(cipher), 64)
    plain = ""
    if (decrypt_package['addition_count']!=0):
        print ("Error: Bits check failed, maybe the cipher you've input was wrong?")
        return
    else:
        for d in decrypt_package["data"]:
            node = DES.decrypt(d, k, silence=True)
            plain += node
    plain = plain[:-int(addition)]
    print (plain)
    print (decode(plain))

# encryptor()
decryptor()