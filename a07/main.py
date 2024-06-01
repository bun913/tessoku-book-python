# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    D, N, deltas = arrange()
    attends = act(D, N , deltas)
    for i in range(D):
        print(attends[i])


def arrange():
    D = int(input())
    N = int(input())
    deltas = [0 for _ in range(D)]
    return D, N, deltas


def act(D, N, deltas):
    for i in range(N):
        l, r = map(int, input().split())
        deltas[l-1] += 1
        if r < len(deltas):
            deltas[r] -= 1
    # 累積和を出す
    attends = [0 for _ in range(D)]
    for i in range(D):
        if i == 0:
            attends[i] = deltas[i]
        else:
            attends[i] = deltas[i] + attends[i-1]
    return attends


solve()
