# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    D, N, L = arrange()
    act(D, N, L)


def arrange():
    D, N = map(int, input().split())
    L = [24 for _ in range(D+1)]
    L[0] = 0
    return D, N, L


def act(D, N, L):
    for _ in range(N):
        l, r, h = map(int, input().split())
        for d in range(l, r+1):
            L[d] = min(L[d], h)
    print(sum(L))


solve()
