# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, S, A = arrange()
    dp = makedp(N, S, A)
    act(dp)


def arrange():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    return N, S, A


def makedp(N, S, A):
    dp = [[False for _ in range(S+1)] for _ in range(N+1)]
    dp[0][0] = True
    # i番目までの要素を使っていときに作れる数をメモしていく
    for i in range(1, N+1):
        card_num = A[i-1]
        for j in range(S+1):
            if dp[i-1][j] is True:
                dp[i][j] = True
                continue
            if j - card_num < 0:
                continue
            if dp[i-1][j-card_num] is True:
                dp[i][j] = True
    return dp


def act(dp):
    for l in dp:
        if l[-1] is True:
            print("Yes")
            exit()
    print("No")


solve()
