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
    for i in range(1, N+1):
        q = deque([i])
        visited = [False] * (N+1)
        while q:
            cur = q.popleft()
            visited[cur] = True
            for nex in graph[cur]:
                if visited[nex] is True:
                    continue
                q.appendleft(nex)
        if False in visited[1:]:
            print("The graph is not connected.")
            exit()
        print("The graph is connected.")
        exit()


solve()
