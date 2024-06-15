# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    S, T = arrange()
    dp = makedp(S, T)
    act(dp)


def arrange():
    S = input()
    T = input()
    return S, T


def makedp(S, T):
    dp = [[0 for _ in range(len(T)+1)] for _ in range(len(S)+1)]
    for i in range(1, len(S)+1):
        for j in range(1, len(T)+1):
            s = S[i-1]
            t = T[j-1]
            if s == t:
                dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp


def act(dp):
    ans = 0
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            ans = max(ans, dp[i][j])
    print(ans)


solve()
