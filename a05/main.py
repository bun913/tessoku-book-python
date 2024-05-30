# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, K = arrange()
    ans = act(N, K)
    print(ans)


def arrange():
    return list(map(int, input().split()))


def act(N, K):
    ans = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            c = K - (a + b)
            if 0 < c <= N:
                ans += 1
    return ans


solve()
