# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N = arrange()
    act(N)


def arrange():
    N = int(input())
    return N


def act(N):
    primse = makeprimes(N)
    for i in range(N+1):
        if primse[i]:
            print(i)


def makeprimes(N):
    primse = [True for _ in range(N+9)]
    primse[0] = False
    primse[1] = False
    for n in range(2, N+1):
        if primse[n] is False:
            continue
        q = n * 2
        while q <= N:
            primse[q] = False
            q += n
    return primse


solve()
