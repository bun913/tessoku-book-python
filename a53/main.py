# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
import heapq

setrecursionlimit(10**8)


def solve():
    Q = arrange()
    act(Q)


def arrange():
    return int(input())


def act(Q):
    q = []
    heapq.heapify(q)
    for _ in range(Q):
        s = input()
        if s.startswith("1"):
            _, x = map(int, s.split())
            heapq.heappush(q, x)
            continue
        if s == "2":
            num = heapq.heappop(q)
            print(num)
            heapq.heappush(q, num)
            continue
        heapq.heappop(q)


solve()
