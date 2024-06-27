# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, K = arrange()
    act(N, K)


def arrange():
    return map(int, input().split())


def act(N, K):
    if K >= 2*N - 2:
        if K % 2 == 0:
            print("Yes")
            exit()
    print("No")


solve()
