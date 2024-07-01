# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from operator import mul
from functools import reduce

setrecursionlimit(10**8)


def solve():
    N, A = arrange()
    act(N, A)


def arrange():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A


def act(N, A):
    memo = enumrate(A)
    ans = 0
    for k, v in memo.items():
        if v < 3:
            continue
        cnt = cmb(v, 3)
        ans += cnt
    print(ans)


def enumrate(A):
    dic = {}
    for a in A:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
    return dic


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    elif r < 0:
        return 0
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


solve()
