# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, Q, Z = arrange()
    act(Q, Z)


def arrange():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    # 累積和で書く点に何個点があったかを記録しておく
    # XYが最大1500なので、1501*1501の配列を用意しておく
    Z = [[0] * (1501) for _ in range(1501)]
    for x, y in xy:
        Z[x][y] += 1
    # 横方向に累積和を取る
    for i in range(1, 1501):
        for j in range(1, 1501):
            Z[i][j] += Z[i][j-1]
    # 縦方向に累積和を取る
    for j in range(1, 1501):
        for i in range(1, 1501):
            Z[i][j] += Z[i-1][j]
    return N, Q, Z


def act(Q, Z):
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        total = Z[c][d] - Z[a-1][d] - Z[c][b-1] + Z[a-1][b-1]
        print(total)


solve()
