# -*- coding: utf-8 -*-
"""
解く前のメモ用# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
# -*- coding: utf-8 -*-
from sys import setrecursionlimit
from bisect import bisect_left, bisect_right

setrecursionlimit(10**8)

MOD = 1000000007


def solve():
    N, W, L, R, X = arrange()
    act(N, W, L, R, X)


def arrange():
    N, W, L, R = map(int, input().split())
    X = list(map(int, input().split()))
    return N, W, L, R, X


def act(N, W, L, R, X):
    goals = [0] + X + [W]
    dp = [0] * len(goals)
    cum_sum = [0] * (len(goals) + 1)
    dp[0] = 1
    cum_sum[1] = 1

    for i in range(1, len(goals)):
        mindis = goals[i] - R
        maxdis = goals[i] - L
        left = bisect_left(goals, mindis)
        right = bisect_right(goals, maxdis) - 1

        if left <= right:
            dp[i] = (cum_sum[right + 1] - cum_sum[left]) % MOD

        cum_sum[i + 1] = (cum_sum[i] + dp[i]) % MOD

    print(dp[-1])


solve()

"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    arrange()
    act()


def arrange():
    pass


def act():
    pass

solve()
