import DES
import random

k = bin(int('FFFFFFFFFFFFFFFA',16))[2:]
c = bin(int('AAAAAFFFFFFFFFFF',16))[2:]
print ("明文",hex(int(c,2)))
p = DES.encrypt(c, k)
print ("密文",hex(int(p,2)))

c1 = DES.decrypt(p, k)
print ("明文",hex(int(c1,2)))

def keygen():
    flag = False
    key = ""
    for i in range(0:64):
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
    return (key)
