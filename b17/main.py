# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, H = arrange()
    dp = makedp(N, H)
    act(N, dp, H)


def arrange():
    N = int(input())
    H = list(map(int, input().split()))
    return N, H


def makedp(N, H):
    dp = [0] * N
    dp[1] = abs(H[1] - H[0])
    for i in range(2, N):
        cand1 = dp[i-1] + abs(H[i] - H[i-1])
        cand2 = dp[i-2] + abs(H[i] - H[i-2])
        dp[i] = min(cand1, cand2)
    return dp


def act(N, dp, H):
    ans = []
    place = N-1
    while True:
        ans.append(place+1)
        if place == 0:
            break
        # 前の足場から来たのか比べる
        if dp[place] == dp[place-1] + abs(H[place]-H[place-1]):
            place -= 1
        else:
            place -= 2
    ans = ans[::-1]
    print(len(ans))
    print(*ans)


solve()
