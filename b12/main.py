# -*- coding: utf-8 -*-
"""
解く前のメモ用
xはたかだか10**2も行かない
早退誤差または絶対誤差が0.001以下であれば正解となる
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N = arrange()
    act(N)


def arrange():
    return int(input())


def act(N):
    ok = 100.0
    ng = 0
    ans = meguru_bisect(ng, ok, N)
    print(ans)


def meguru_bisect(ng, ok, N):
    while (ok-ng > 0.001):
        mid = (ok+ng)/2
        if is_ok(mid, N):
            ok = mid
        else:
            ng = mid
    return ok


def is_ok(x, N):
    if x * x * x + x >= N:
        return True


solve()
