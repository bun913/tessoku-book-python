# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, A = arrange()
    act(N, A)


def arrange():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A


def act(N, A):
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                a = A[i]
                b = A[j]
                c = A[k]
                if a + b + c == 1000:
                    print("Yes")
                    exit()
    print("No")


solve()
