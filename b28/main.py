# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)

MOD = 10**9+7


def solve():
    N = arrange()
    fibos = makefib(N)
    act(N, fibos)


def arrange():
    return int(input())
    pass


def makefib(N):
    fibos = [0 for _ in range(N+9)]
    fibos[1] = 1
    fibos[2] = 1
    for i in range(3, N+1):
        fibos[i] = (fibos[i-1] + fibos[i-2]) % MOD
    return fibos


def act(N, fibos):
    print(fibos[N])


solve()
