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
    dist = [float('inf')] * N
    # 頂点1からの頂点1までの距離は0にする
    dist[0] = 0
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, 0))
    while q:
        # 今の頂点から最も近い頂点を取り出す
        cost, cur = heapq.heappop(q)
        if cost > dist[cur]:
            continue
        for nex_cost, nex in graph[cur]:
            # distがより短い距離で行ける場合は更新する
            if dist[nex] > dist[cur] + nex_cost:
                dist[nex] = dist[cur] + nex_cost
                # キューに対してまた近い頂点が取り出せるようになる
                heapq.heappush(q, (dist[nex], nex))
    for d in dist:
        if d == float('inf'):
            print(-1)
            continue
        print(d)


def make_graph(N, M):
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a, b = a-1, b-1
        # (cost, node) の形で格納する
        graph[a].append((c, b))
        graph[b].append((c, a))
    return graph


solve()
