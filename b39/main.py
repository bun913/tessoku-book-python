# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from collections import deque
import heapq

setrecursionlimit(10**8)


def solve():
    N, D, XY = arrange()
    act(N, D, XY)


def arrange():
    N, D = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]
    return N, D, XY


def act(N, D, XY):
    # i日目から受けられる仕事をメモしておく
    memo = [[] for _ in range(D+1)]
    for x, y in XY:
        memo[x].append(y)
    q = []
    heapq.heapify(q)
    ans = 0
    for d in range(D):
        jobs = memo[d+1]
        for job in jobs:
            # マイナスを入れて最大値を取り出せるようにする
            heapq.heappush(q, -job)
        if q:
            ans += -heapq.heappop(q)
    print(ans)


solve()
