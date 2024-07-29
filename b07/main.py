# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    T, N, deltas = arrange()
    act(T, N, deltas)


def arrange():
    T = int(input())
    N = int(input())
    deltas = [0 for _ in range(T)]
    return T, N, deltas


def act(T, N, deltas):
    for i in range(N):
        l, r = map(int, input().split())
        deltas[l] += 1
        if r < len(deltas):
            deltas[r] -= 1
    # 累積和を出す
    timings = [0 for _ in range(T)]
    for i in range(T):
        if i == 0:
            timings[i] = deltas[i]
        else:
            timings[i] = deltas[i] + timings[i-1]
    # 結果を出力する
    for t in timings:
        print(t)


solve()
