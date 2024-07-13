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
    N, M = map(int, input().split())
    return N, M


def act(N, M):
    g = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    for i in range(1, N):
        s = ", ".join(map(str, g[i]))
        print(str(i) + ": {"+s + "}")


solve()
