# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    S = arrange()
    ans = act(S)
    print(ans)


def arrange():
    return input()


def act(S):
    L = list(S)
    L = [int(l) for l in L]
    # 逆にして処理
    L = L[::-1]
    i = 0
    ans = 0
    for l in L:
        ans += 2 ** i * l
        i += 1
    return ans


solve()
