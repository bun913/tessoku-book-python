# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    A, B = arrange()
    act(A, B)


def arrange():
    return list(map(int, input().split()))


def act(A, B):
    ans = gcd(A, B)
    print(ans)


def gcd(a, b):
    big, small = max(a, b), min(a, b)
    if small == 0:
        return big
    return gcd(small, big % small)


solve()
