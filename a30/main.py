# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    n, r = arrange()
    act(n, r)


def arrange():
    return map(int, input().split())


def act(n, r):
    MOD = 10**9 + 7
    num = 1
    for i in range(1, n+1):
        num = num * i % MOD
    dem = 1
    for i in range(1, r+1):
        dem = dem * i % MOD
    for i in range(1, n-r+1):
        dem = dem * i % MOD
    # 逆元を求める
    dem = pow(dem, MOD-2, MOD)
    ans = num * dem % MOD
    print(ans)


solve()
