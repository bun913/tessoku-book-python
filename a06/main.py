# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, Q, A, S = arrange()
    act(N, Q, S)


def arrange():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0 for _ in range(N)]
    for i in range(N):
        a = A[i]
        if i == 0:
            S[i] = a
        else:
            S[i] = S[i-1] + a
    return N, Q, A, S


def act(N, Q, S):
    for q in range(Q):
        l, r = map(int, input().split())
        if l == 1:
            print(S[r-1])
            continue
        print(S[r-1] - S[l-2])


solve()
