# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, Q = arrange()
    act(N, Q)


def arrange():
    return map(int, input().split())


def act(N, Q):
    L = [i for i in range(1, N+1)]
    is_revers = False
    for j in range(Q):
        q = input()
        # 反転を制御
        if q == "2":
            is_revers = not is_revers
            continue
        if q.startswith("1"):
            _, x, y = q.split(" ")
            x, y = int(x), int(y)
            if is_revers is False:
                L[x-1] = y
            else:
                L[N-x] = y
        else:
            _, x = q.split(" ")
            if is_revers is False:
                print(L[int(x)-1])
            else:
                print(L[N-int(x)])


solve()
