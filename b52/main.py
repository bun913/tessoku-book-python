# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from collections import deque

setrecursionlimit(10**8)


def solve():
    N, X, A = arrange()
    act(N, X, A)


def arrange():
    N, X = map(int, input().split())
    A = list(input())
    return N, X, A


def act(N, X, A):
    # 操作1 キューに入れてX番目のボールを青くする
    X -= 1
    q = deque([X])
    q.append(X)
    A[X] = "@"
    while q:
        # キューの先頭を取り出す
        pos = q.popleft()
        if pos-1 >= 0 and A[pos-1] == ".":
            A[pos-1] = "@"
            q.appendleft(pos-1)
        if pos + 1 < N and A[pos+1] == ".":
            A[pos+1] = "@"
            q.appendleft(pos+1)
    print(*A, sep="")


solve()
