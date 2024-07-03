# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, K, AB = arrange()
    act(N, K, AB)


def arrange():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    return N, K, AB


def act(N, K, AB):
    ans = 0
    for x in range(1, 101):
        for y in range(1, 101):
            joinable = enumrate_joinable_members(x, y, K, AB)
            ans = max(ans, joinable)
    print(ans)


def enumrate_joinable_members(x, y, K, AB):
    cnt = 0
    for a, b in AB:
        if (x <= a and a <= x+K and y <= b and b <= y+K):
            cnt += 1
    return cnt


solve()
