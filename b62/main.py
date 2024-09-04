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
    # グラフを作成
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    q = deque([1])
    visited = [False] * (N+1)
    parent = [-1] * (N+1)
    # 深さ優先探索で経路を探す
    while q:
        cur = q.popleft()
        visited[cur] = True
        for nex in graph[cur]:
            if visited[nex] is True:
                continue
            parent[nex] = cur
            q.append(nex)
    # 経路を復元
    path = []
    node = N
    while node != -1:
        path.append(node)
        node = parent[node]
    print(*path[::-1])


solve()
