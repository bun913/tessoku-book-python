# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from collections import deque

setrecursionlimit(10**8)


def solve():
    N, D, XY = arrange()
    act(N, D, XY)


def arrange():
    N, D = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]
    return N, D, XY


def act(N, D, XY):
    used = [False] * N
    ans = 0
    for d in range(D):
        # i日目の仕事を順に見ていく
        max_value = 0
        max_id = -1
        # 仕事を全部見ていく
        for j in range(N):
            # もうとっている仕事なら飛ばす
            if used[j] is True:
                continue
            # 仕事がd日目に選べるもので、最も報酬が高いものを選ぶ
            if max_value < XY[j][1] and XY[j][0] <= d+1:
                max_value = XY[j][1]
                max_id = j
        if max_id != -1:
            ans += max_value
            used[max_id] = True
    print(ans)


solve()
