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


def my_pow(a, b, mod):
    ans = 1
    # bが0になるまでaをmodで割りながら掛け算していく
    while b > 0:
        # bの最下位ビットが1のときはa(2**n)をかける
        # つまり10進数を2進数に変換して、1の位が1のときにaをかけるというやつ
        if b & 1:
            ans = ans * a % mod
        a = a * a % mod
        b >>= 1
    return ans


solve()
