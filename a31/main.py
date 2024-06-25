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
    return int(input())


def act(N):
    n3 = N // 3
    n5 = N // 5
    n15 = N // 15
    ans = n3 + n5 - n15
    print(ans)


solve()
