# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    a, b = arrange()
    act(a, b)


def arrange():
    return map(int, input().split())


def act(a, b):
    ans = my_pow(a, b, 10**9 + 7)
    print(ans)


def my_pow(x, y, mod):
    ans = 1
    while y > 0:
        if y & 1:
            ans = ans * x % mod
        x = x * x % mod
        y >>= 1
    return ans


solve()
