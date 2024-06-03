# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    H, W, Z = arrange()
    act(H, W, Z)


def arrange():
    H, W, N = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(N)]
    # 前日比を取るための二次元配列を作成
    Z = [[0] * (W+2) for _ in range(H+2)]
    # 前との差分を取る
    for a, b, c, d in ab:
        Z[a][b] += 1
        Z[a][d+1] -= 1
        Z[c+1][b] -= 1
        Z[c+1][d+1] += 1
    # 横の累積和を取る
    for i in range(1, H+1):
        for j in range(1, W+1):
            Z[i][j] += Z[i][j-1]
    # 縦の累積和を取る
    for j in range(1, W+1):
        for i in range(1, H+1):
            Z[i][j] += Z[i-1][j]
    return H, W, Z


def act(H, W, Z):
    for i in range(1, H+1):
        tmp = []
        for j in range(1, W+1):
            tmp.append(str(Z[i][j]))
        print(*tmp)


solve()
