# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from collections import deque

setrecursionlimit(10**8)


def solve():
    R, C, start, goal = arrange()
    act(R, C, start, goal)


def arrange():
    R, C = map(int, input().split())
    start = list(map(int, input().split()))
    start[0] -= 1
    start[1] -= 1
    goal = list(map(int, input().split()))
    goal[0] -= 1
    goal[1] -= 1
    return R, C, start, goal


def act(R, C, start, goal):
    graph = make_graph(R, C)
    q = deque([start[0]*C + start[1]])
    dist = [-1 for _ in range(R*C)]
    dist[start[0]*C + start[1]] = 0
    while q:
        cur = q.popleft()
        # ゴールに着いたら終わり
        if cur == goal[0]*C + goal[1]:
            break
        for nex in graph[cur]:
            if dist[nex] != -1:
                continue
            dist[nex] = dist[cur] + 1
            q.append(nex)
    print(dist[goal[0]*C + goal[1]])


def make_graph(R, C):
    graph = [[] for _ in range(R*C)]
    # 迷路の入力を受け取る
    grid = [list(input()) for _ in range(R)]
    # グラフを作成
    for i in range(R):
        for j in range(C):
            if grid[i][j] == "#":
                continue
            for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni, nj = i + direction[0], j + direction[1]
                # 迷路の範囲内か確認
                if ni >= 0 and ni < R and nj >= 0 and nj < C:
                    if grid[ni][nj] == ".":
                        graph[i*C + j].append(ni*C + nj)
    return graph


solve()
