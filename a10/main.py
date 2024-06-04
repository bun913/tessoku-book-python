# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    D, LR,  max_left, max_right = arrange()
    act(D, LR, max_left, max_right)


def arrange():
    N = int(input())
    A = list(map(int, input().split()))
    D = int(input())
    LR = [list(map(int, input().split())) for _ in range(D)]
    # 左から見た時の累積Maxを作っておく
    max_left = [0] * N
    for i in range(N):
        if i == 0:
            max_left[i] = A[i]
            continue
        max_left[i] = max(A[i], max_left[i-1])
    # 右から見た時の累積Maxを作っておく
    max_right = [0] * N
    for j in range(N-1, -1, -1):
        if j == N-1:
            max_right[j] = A[j]
            continue
        max_right[j] = max(A[j], max_right[j+1])
    return D, LR, max_left, max_right


def act(D, LR, max_left, max_right):
    for d in range(D):
        l, r = LR[d]
        cand1 = max_left[l-2]
        cand2 = max_right[r]
        print(max(cand1, cand2))


solve()
