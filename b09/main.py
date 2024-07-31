# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    Z = arrange()
    act(Z)


def arrange():
    N = int(input())
    abcd = [list(map(int, input().split())) for _ in range(N)]
    # 紙を置くのに十分な二次元空間を再現
    Z = [[0]*1509 for _ in range(1509)]
    # 紙の始点に1を足し、累積和を取れるようにする
    # Zは座標i+0.5, j+0.5に紙があるかどうかを表す
    for a, b, c, d in abcd:
        Z[a][b] += 1
        Z[a][d] -= 1
        Z[c][b] -= 1
        Z[c][d] += 1
    # 累積和を取る
    # 横の累積和
    for i in range(0, 1509):
        for j in range(0, 1509):
            Z[i][j] += Z[i][j-1]
    # 縦の累積和
    for j in range(0, 1509):
        for i in range(0, 1509):
            Z[i][j] += Z[i-1][j]
    return Z


def act(Z):
    ans = 0
    for i in range(len(Z)):
        for j in range(len(Z)):
            if Z[i][j] > 0:
                ans += 1
    print(ans)


solve()
