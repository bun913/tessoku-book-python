# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    H, W, grid = arrange()
    act(H, W, grid)


def arrange():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    return H, W, grid


def act(H, W, grid):
    dp = [[0] * (W+1) for _ in range(H+1)]
    dp[0][1] = 1
    for i in range(1, H+1):
        for j in range(1, W+1):
            cur = grid[i-1][j-1]
            if cur == "#":
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[H][W])


solve()
