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
    gcd_num = gcd(max(A, B), min(A, B))
    ans = A * B // gcd_num
    print(ans)


def gcd(big, small):
    if small == 0:
        return big
    return gcd(small, big % small)


solve()
