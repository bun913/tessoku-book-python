# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, M, B, A, C = arrange()
    act(N, M, B, A, C)


def arrange():
    N, M, B = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    return N, M, B, A, C


def act(N, M, B, A, C):
    # まずはBを通る合計を算出
    sum_b = B * N * M
    # 次にAを足される回数から算出
    sum_a = 0
    for a in A:
        sum_a += a * M
    sum_c = 0
    for c in C:
        sum_c += c * N
    ans = sum_b + sum_a + sum_c
    print(ans)


solve()
