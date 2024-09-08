# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from collections import defaultdict

setrecursionlimit(10**8)


def solve():
    N, M, A = arrange()
    act(N, M, A)


def arrange():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    return N, M, A


def act(N, M, A):
    memo = defaultdict(int)
    for a in A:
        memo[a] += 1
    for i in range(N):
        print(M - memo[i+1])


solve()
