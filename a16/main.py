# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, A, B = arrange()
    act(N, A, B)


def arrange():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    return N, A, B


def act(N, A, B):
    dp = [0] * N
    for i in range(1, N):
        if i == 1:
            dp[i] = A[0]
            continue
        cand1 = dp[i-1] + A[i-1]
        cand2 = dp[i-2] + B[i-2]
        dp[i] = min(cand1, cand2)
    print(dp[-1])


solve()
