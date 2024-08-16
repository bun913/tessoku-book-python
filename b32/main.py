# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, K, A = arrange()
    act(N, K, A)


def arrange():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    return N, K, A


def act(N, K, A):
    is_wins = [False] * (N+1)
    for n in range(1, N+1):
        for a in A:
            if n-a >= 0 and is_wins[n-a] is False:
                is_wins[n] = True
                break
    if is_wins[N] is True:
        print("First")
        exit()
    print("Second")


solve()
