# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, A = arrange()
    act(A)


def arrange():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    return N, A


def act(A):
    Q = int(input())
    for _ in range(Q):
        x = int(input())
        ok = -1
        ng = len(A)
        ind = meguru_bisect(ok, ng, A, x)
        print(ind+1)


def meguru_bisect(ok, ng, A, x):
    while (abs(ok-ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(x, A[mid]):
            ok = mid
        else:
            ng = mid
    return ok


def is_ok(x, cur):
    return cur < x


solve()
