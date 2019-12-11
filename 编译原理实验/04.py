# -*- coding:gbk -*-
E = "TX"
X = "$|+T|-T"
T = "FZ"
Z = "$|*F|/F"
F = "(E)|a|b|c"
lx = X.split("|")
lz = Z.split("|")
lf = F.split("|")
le = [E]
lt = [T]
tDict = {"E": le, "X": lx, "T": lt, "Z": lz, "F": lf}
U = lx + lf + lz + le + lt

Vn = set("#", )
Vt = set()
for i in U:
    for j in i:
        if not j.isupper():
            Vn.add(j)
        else:
            Vt.add(j)


def panDuan(m, ins, i):
    if len(m) == 0 and i == len(ins):
        print(ins + "       success")
        return True
    elif len(m) == 0 or i == len(ins):
        print(ins + "       error")
        return True


def vn(ins, i):
    if ins[i] not in Vn:
        print(ins + "       error")
        exit(0)


def Ee(s, ins, i):
    vn(ins, i)
    s = s[1::]
    s = "TX" + s
    Tt(s, ins, i)


def Tt(s, ins, i):
    vn(ins, i)
    s = s[1::]
    s = "FZ" + s
    F(s, ins, i)


def d(m, ins, i):
    if m[0] == "E":
        Ee(m, ins, i)
    elif m[0] == "X":
        X(m, ins, i)
    elif m[0] == "Z":
        Z(m, ins, i)
    elif m[0] == "T":
        Tt(m, ins, i)
    elif m[0] == "F":
        F(m, ins, i)


def F(s, ins, i):
    vn(ins, i)
    s = s[1::]
    for j in lf:
        m = j + s
        if m[0] == ins[i]:
            while m[0] == ins[i]:
                m = m[1::]
                i += 1
                if panDuan(m, ins, i):
                    return
            d(m, ins, i)


def Z(s, ins, i):
    vn(ins, i)
    s = s[1::]
    for j in lz:
        m = j + s
        if m[0] == "$":
            m = m[1::]
            while m[0] == ins[i]:
                m = m[1::]
                i += 1
                if panDuan(m, ins, i):
                    return
            d(m, ins, i)
        elif m[0] == ins[i]:
            while m[0] == ins[i]:
                m = m[1::]
                i += 1
                if panDuan(m, ins, i):
                    return
            d(m, ins, i)


def X(s, ins, i):
    vn(ins, i)
    s = s[1::]
    for j in lx:
        m = j + s
        if m[0] == "$":
            m = m[1::]
            while m[0] == ins[i]:
                m = m[1::]
                i += 1
                if panDuan(m, ins, i):
                    return
            d(m, ins, i)
        elif m[0] == ins[i]:
            while m[0] == ins[i]:
                m = m[1::]
                i += 1
                if panDuan(m, ins, i):
                    return
            d(m, ins, i)


S = "E#"
s1 = "(a+b)*d#"
# s1 = input("请输入字符串(以#结束)：")
Ee(S, s1, 0)
