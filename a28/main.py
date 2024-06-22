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
    mod = 10000
    ans = 0
    for _ in range(N):
        t, a = input().split()
        a = int(a)
        if t == "+":
            ans += a
            ans %= mod
        elif t == "-":
            ans -= a
            ans %= mod
        else:
            ans *= a
            ans %= mod
        print(ans)


solve()
