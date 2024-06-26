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
    return map(int, input().split())


def act(N, A, B):
    dp = [False] * (N + 1)
    for n in range(min(A, B, N), N+1):
        if n - A >= 0 and dp[n-A] is False:
            dp[n] = True
        if n - B >= 0 and dp[n-B] is False:
            dp[n] = True
    if dp[N] is True:
        print("First")
        exit()
    print("Second")


solve()
