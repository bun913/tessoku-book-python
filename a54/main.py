# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    Q = arrange()
    act(Q)


def arrange():
    return int(input())


def act(Q):
    memo = {}
    for _ in range(Q):
        s = input()
        if s.startswith("1"):
            _, key, value = s.split()
            memo[key] = value
            continue
        _, key = s.split()
        print(memo[key])


solve()
