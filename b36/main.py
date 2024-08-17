# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, K, S = arrange()
    act(N, K, S)


def arrange():
    N, K = map(int, input().split())
    S = input()
    return N, K, S


def act(N, K, S):
    on_cnt = 0
    for s in S:
        if s == "1":
            on_cnt += 1
    if on_cnt % 2 == K % 2:
        print("Yes")
        exit()
    print("No")


solve()
