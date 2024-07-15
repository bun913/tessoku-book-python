# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from collections import deque

setrecursionlimit(10**8)


def solve():
    N, M = arrange()
    act(N, M)


def arrange():
    return map(int, input().split())


def act(N, M):
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # 頂点1から頂点kまでの最短距離を保存する
    dis = [-1 for _ in range(N+1)]
    dis[0] = 0
    dis[1] = 0
    q = deque([1])
    while q:
        cur = q.pop()
        for nex in graph[cur]:
            if dis[nex] != -1:
                continue
            dis[nex] = dis[cur] + 1
            q.appendleft(nex)
    for i in range(1, N+1):
        print(dis[i])


solve()
