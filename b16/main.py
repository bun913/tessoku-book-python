# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, H = arrange()
    act(N, H)


def arrange():
    N = int(input())
    H = list(map(int, input().split()))
    return N, H


def act(N, H):
    dp = [0] * N
    dp[1] = abs(H[1] - H[0])
    for i in range(2, N):
        bef1 = dp[i-1] + abs(H[i]-H[i-1])
        bef2 = dp[i-2] + abs(H[i]-H[i-2])
        dp[i] = min(bef1, bef2)
    print(dp[-1])


solve()
