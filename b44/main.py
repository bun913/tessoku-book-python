# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, A = arrange()
    act(N, A)


def arrange():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    return N, A


def act(N, A):
    # i行目の行が今どの行に交換されているかを管理する
    row_cnts = [i for i in range(N)]
    Q = int(input())
    for _ in range(Q):
        q, x, y = map(int, input().split())
        if q == 1:
            row_cnts[x-1], row_cnts[y-1] = row_cnts[y-1], row_cnts[x-1]
            continue
        # 取得操作
        a = row_cnts[x-1]
        print(A[a][y-1])


solve()
