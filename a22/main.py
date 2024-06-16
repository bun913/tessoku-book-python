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
    dp = [-(10**9)] * (N + 1)
    dp[1] = 0
    for i in range(1, N):
        dp[A[i-1]] = max(dp[A[i-1]], dp[i]+100)
        dp[B[i-1]] = max(dp[B[i-1]], dp[i]+150)
    print(dp[N])


solve()
