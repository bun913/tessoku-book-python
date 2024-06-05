# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, X, A = arrange()
    act(N, X, A)


def arrange():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    return N, X, A


def act(N, X, A):
    ok = -1
    ng = N
    ng, ok = meguru_bisect(ng, ok, X, A)
    print(ng)


def meguru_bisect(ng, ok, X, A):
    while (abs(ok-ng) > 1):
        mid = (ok+ng) // 2
        if is_ok(mid, A, X):
            ok = mid
        else:
            ng = mid
    return ng, ok


def is_ok(mid, A, X):
    return A[mid] <= X


solve()
