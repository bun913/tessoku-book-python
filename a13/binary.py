# -*- coding: utf-8 -*-
"""
解く前のメモ用
二部探索で解いた時の解法
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
    ans = 0
    for i in range(N):
        ok = i
        ng = N
        ind = meguru_bisect(i, ok, ng, K, A)
        ans += ind-i
    print(ans)


def meguru_bisect(i, ok, ng, K, A):
    while (abs(ok-ng) > 1):
        mid = (ok+ng)//2
        if is_ok(A[i], A[mid], K):
            ok = mid
        else:
            ng = mid
    return ok


def is_ok(cur, cand, K):
    return abs(cand-cur) <= K


solve()
