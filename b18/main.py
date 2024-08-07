# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, S, A = arrange()
    dp = makedp(N, S, A)
    act(N, S, A, dp)


def arrange():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    return N, S, A


def makedp(N, S, A):
    dp = [[False for _ in range(S+1)] for _ in range(N+1)]
    dp[0][0] = True
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


def act(N, S, A, dp):
    # 最後尾から逆に確認していく
    target = S
    if dp[N][S] is False:
        print(-1)
        return
    ans = []
    for i in range(N, 0, -1):
        cur = A[i-1]
        if target >= cur and dp[i-1][target-cur] is True:
            ans.append(i)
            target -= cur
    print(len(ans))
    print(*ans[::-1])


solve()
