# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    a, b, c = arrange()
    act(a, b, c)


def arrange():
    return map(int, input().split())


def act(a, b, c):
    if sum([a, b, c]) == 0:
        print("Yes")
        exit()
    print("No")


solve()
