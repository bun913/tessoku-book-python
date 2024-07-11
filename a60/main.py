# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from collections import deque

setrecursionlimit(10**8)


def solve():
    N, A = arrange()
    act(N, A)


def arrange():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A


def act(N, A):
    q = deque([])
    ans = []
    for d in range(N):
        # 1日目は絶対に-1になる
        if d == 0:
            ans.append(-1)
            q.append((A[d], d+1))
            continue
        while q:
            comp = q.popleft()
            if comp[0] > A[d]:
                q.appendleft(comp)
                ans.append(comp[1])
                break
        q.appendleft((A[d], d+1))
    print(*ans)


solve()
