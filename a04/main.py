# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N = arrange()
    ans = act(N)
    print(*ans, sep="")


def arrange():
    return int(input())


def act(N):
    n = N
    l = []
    while n >= 2:
        rest = n % 2
        l = [rest] + l
        n = n // 2
    l = [n] + l
    # 10桁になるまで0を追加
    while len(l) < 10:
        l = [0] + l
    return l


solve()
