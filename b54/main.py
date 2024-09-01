# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, memo = arrange()
    act(memo)


def arrange():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    memo = {}
    for a in A:
        if a in memo:
            memo[a] += 1
        else:
            memo[a] = 1
    return N, memo


def act(memo):
    ans = 0
    for k, v in memo.items():
        if v < 2:
            continue
        ans += v * (v - 1) // 2
    print(ans)


solve()
