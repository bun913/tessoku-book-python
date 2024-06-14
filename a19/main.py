# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, W, wv = arrange()
    dp = makedp(N, W, wv)
    act(dp)


def arrange():
    N, W = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(N)]
    return N, W, wv


def makedp(N, W, wv):
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        w, v = wv[i-1]
        for j in range(W+1):
            if j < w:
                dp[i][j] = dp[i-1][j]
                continue
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
    return dp


def act(dp):
    print(dp[-1][-1])


solve()
