# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, A, B = arrange()
    act(N, A, B)


def arrange():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort(reverse=True)
    return N, A, B


def act(N, A, B):
    ans = 0
    for i in range(N):
        a = A[i]
        b = B[i]
        ans += a*b
    print(ans)


solve()
