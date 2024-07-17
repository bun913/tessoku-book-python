# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, A = arrange()
    act(N, A)


def arrange():
    N = int(input())
    A = [0] * 2 + list(map(int, input().split()))
    return N, A


def act(N, A):
    graph = make_graph(N, A)
    # 部下の数をメモする動的計画法の配列
    dp = [0 for _ in range(N+1)]
    for i in range(N, 0, -1):
        for buka in graph[i]:
            dp[i] += dp[buka] + 1
    print(*dp[1:])


def make_graph(N, A):
    graph = [[] for _ in range(N+1)]
    for i in range(2, N+1):
        # 上司から部下の方向にグラフを貼る
        a = A[i]
        graph[a].append(i)
    return graph


solve()
