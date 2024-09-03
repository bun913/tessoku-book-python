# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, M = arrange()
    act(N, M)


def arrange():
    return map(int, input().split())


def act(N, M):
    g = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    # 友達の数が多い人を求める
    cnt = 0
    ans = 1
    for i in range(1, N+1):
        l = g[i]
        if len(l) > cnt:
            cnt = len(l)
            ans = i
    print(ans)


solve()
