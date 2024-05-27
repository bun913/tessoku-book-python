# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, X, A = arrange()
    act(X, A)


def arrange():
    N, X = list(map(int, input().split()))
    A = list(map(int, input().split()))
    return N, X, A


def act(X, A):
    ans = "No"
    for a in A:
        if a == X:
            ans = "Yes"
            break
    print(ans)


solve()
