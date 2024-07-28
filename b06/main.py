# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, A, S, Q =arrange()
    act(N, Q, S)


def arrange():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0 for _ in range(N)]
    for i in range(N):
        if i == 0:
            S[i] = A[i]
        else:
            S[i] = S[i-1] + A[i]
    Q = int(input())
    # 累積和の先頭に0を追加
    S = [0] + S
    return N, A, S, Q


def act(N,Q, S):
    for _ in range(Q):
        l, r = map(int, input().split())
        win_point = S[r] - S[l-1]
        day_cnt = r - l + 1
        lose_point = day_cnt - win_point
        if win_point > lose_point:
            print("win")
        elif win_point == lose_point:
            print("draw")
        else:
            print("lose")


solve()
