# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from collections import deque

setrecursionlimit(10**8)


def solve():
    S = arrange()
    act(S)


def arrange():
    return input()


def act(S):
    q = deque([])
    ans = []
    for i in range(len(S)):
        s = S[i]
        if s == "(":
            q.appendleft(i+1)
            continue
        l = q.popleft()
        ans.append((l, i+1))
    for l, r in ans:
        print(l, r)


solve()
