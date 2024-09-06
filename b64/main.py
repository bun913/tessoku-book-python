# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
import heapq

setrecursionlimit(10**8)


def solve():
    N, M = arrange()
    act(N, M)


def arrange():
    return map(int, input().split())


def act(N, M):
    graph = make_graph(N, M)
    # ノード1からの距離を記録する
    dist = [float("inf")] * N
    dist[0] = 0
    # どのノードから来たかを記録する
    parents = [-1] * N
    parents[0] = -1
    q = [(0, 0)]
    heapq.heapify(q)
    while q:
        cost, cur = heapq.heappop(q)
        # すでに確定している場合は飛ばす
        if dist[cur] < cost:
            continue
        for nex_cost, nex in graph[cur]:
            # すでにより短い経路が見つかっている場合は飛ばす
            if dist[nex] < cost + nex_cost:
                continue
            dist[nex] = cost + nex_cost
            parents[nex] = cur
            heapq.heappush(q, (dist[nex], nex))
    # 経路を復元する
    cur = N - 1
    ans = []
    while cur != -1:
        ans.append(cur+1)
        cur = parents[cur]
    print(*ans[::-1])


def make_graph(N, M):
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a, b = a-1, b-1
        graph[a].append((c, b))
        graph[b].append((c, a))
    return graph


solve()
