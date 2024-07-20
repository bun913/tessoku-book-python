# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from bisect import bisect_left

setrecursionlimit(10**8)


def solve():
    N, W, L, R, X = arrange()
    act(N, W, L, R, X)


def arrange():
    N, W, L, R, X = map(int, input().split())
    X = list(map(int, input().split()))
    return N, W, L, R, X


def act(N, W, L, R, X):
    goals = [0] + X[:] + [W]
    can_jump = [False] * len(goals)
    can_jump[0] = True
    dp = [0] * len(goals)
    for i in range(len(goals)):
        # 今いる地点がそもそも来れないなら数える意味がない
        cur = goals[i]
        if can_jump[i] is False:
            continue
        mindis = cur + L
        maxdis = cur + R
        # 今いる地点から行ける最低の地点と最高の地点を求める
        left = bisect_left(goals, mindis)
        if mindis <= goals[left] <= maxdis:
            can_jump[left] = True
            dp[left] += 1
        right = bisect_left(goals, maxdis)
        if mindis <= goals[right] <= maxdis:
            can_jump[right] = True
            dp[right] += 1
    # 累積和を取る
    for i in range(1, len(dp)):
        dp[i] += dp[i - 1]
    print(dp[-1])


solve()
