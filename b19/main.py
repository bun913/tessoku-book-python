# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, W, wv = arrange()
    dp = makedp(N, W, wv)
    act(dp, N, W)


def arrange():
    N, W = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(N)]
    return N, W, wv


def makedp(N, W, wv):
    max_value = N * 1000 + 1
    dp = [[float("inf") for _ in range(max_value)] for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(1, N+1):
        w, v = wv[i-1]
        for j in range(max_value):
            dp[i][j] = dp[i-1][j]
            if j >= v:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-v]+w)
    return dp


def act(dp, N, W):
    ans = 0
    for j in range(len(dp[N])):
        if dp[N][j] <= W:
            ans = j
    print(ans)


solve()
