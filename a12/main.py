# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    K, A = arrange()
    act(K, A)


def arrange():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    return K, A


def act(K, A):
    ok = 10**9
    ng = 0
    ans = meguru_bisect(ng, ok, K, A)
    print(ans)


def meguru_bisect(ng, ok, K, A):
    while (abs(ok - ng) > 1):
        cur_sec = (ok + ng) // 2
        if is_ok(A, K, cur_sec):
            ok = cur_sec
        else:
            ng = cur_sec
    return ok


def is_ok(A, K, cur_sec):
    papers = cur_papers(A, cur_sec)
    return papers >= K


def cur_papers(A, cur_sec):
    papers = 0
    for j in range(len(A)):
        set_of = cur_sec // A[j]
        papers += set_of
    return papers


solve()
