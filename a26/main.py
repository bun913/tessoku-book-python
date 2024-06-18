# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    Q = arrange()
    primse = makeprime()
    act(primse, Q)


def arrange():
    return int(input())


def makeprime():
    primse = [True for _ in range(300001)]
    primse[0] = False
    primse[1] = False
    for n in range(2, 300001):
        if primse[n] is False:
            continue
        q = n * 2
        while q <= 300000:
            primse[q] = False
            q += n
    return primse


def act(primse, Q):
    for _ in range(Q):
        x = int(input())
        if primse[x] is True:
            print("Yes")
        else:
            print("No")


solve()
