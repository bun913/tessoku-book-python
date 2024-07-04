# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, L, AB = arrange()
    act(N, L, AB)


def arrange():
    N, L = map(int, input().split())
    AB = [list(input().split()) for _ in range(N)]
    return N, L, AB


def act(N, L, AB):
    ans = -1
    for a, b in AB:
        rest = 0
        if b == "E":
            rest = L - int(a)
        else:
            rest = int(a)
        ans = max(ans, rest)
    print(ans)


solve()
