# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from collections import deque

setrecursionlimit(10**8)


def solve():
    Q = arrange()
    act(Q)


def arrange():
    return int(input())


def act(Q):
    q = deque([])
    for _ in range(Q):
        s = input()
        if s.startswith("1"):
            _, book = s.split(" ")
            q.appendleft(book)
        elif s == "2":
            print(q[0])
        else:
            q.popleft()


solve()
