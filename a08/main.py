# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    H, W, xy, Q, accum = arrange()
    act(xy, Q, accum)


def arrange():
    H, W = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(H)]
    Q = int(input())
    # 二次元の累積和用の表を作る
    # 表の長さ、高さはそれぞれH+1, W+1としておく
    accum = [[0] * (W+1) for _ in range(H+1)]
    # まずは横方向に累積和を取る
    for i in range(1, H+1):
        for j in range(1, W+1):
            accum[i][j] = accum[i][j-1] + xy[i-1][j-1]
    # 縦方向に累積和を取る
    for j in range(1, W+1):
        for i in range(H+1):
            accum[i][j] += accum[i-1][j]
    return H, W, xy, Q, accum


def act(xy, Q, accum):
    for q in range(Q):
        a, b, c, d = map(int, input().split())
        total = accum[c][d] - accum[a-1][d] - accum[c][b-1] + accum[a-1][b-1]
        print(total)


solve()
