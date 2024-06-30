# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, lr = arrange()
    act(N, lr)


def arrange():
    N = int(input())
    lr = [list(map(int, input().split())) for _ in range(N)]
    return N, lr


def act(N, lr):
    # lrをrの順でソートする
    lr.sort(key=lambda x: x[1])
    # あとは終了時刻と開始時刻を貪欲に見比べていく
    ans = 0
    cur = 0  # 現在時刻
    for i in range(N):
        l, r = lr[i]
        if cur <= l:
            ans += 1
            cur = r
    print(ans)


solve()
