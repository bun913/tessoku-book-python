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
    ans = "No"
    for i in range(A, B+1):
        if 100 % i == 0:
            ans = "Yes"
            break
    print(ans)


solve()
