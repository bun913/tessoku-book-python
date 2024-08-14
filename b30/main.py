# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    H, W = arrange()
    act(H, W)


def arrange():
    return map(int, input().split())


def act(H, W):
    MOD = 10**9 + 7
    num = 1
    for i in range(1, H+W-1):
        num = num * i % MOD
    dem = 1
    for i in range(1, H):
        dem = dem * i % MOD
    for j in range(1, W):
        dem = dem * j % MOD
    # 逆元を求める
    gya = pow(dem, MOD-2, MOD)
    ans = num * gya % MOD
    print(ans)


solve()
