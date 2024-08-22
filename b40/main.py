# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from collections import defaultdict

setrecursionlimit(10**8)


def solve():
    N, A = arrange()
    act(N, A)


def arrange():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A


def act(N, A):
    memo = enumrate(A)
    ans = 0
    for i in range(1, 50):
        ans += memo[i] * memo[100 - i]
    ans += memo[0] * (memo[0] - 1) // 2
    ans += memo[50] * (memo[50] - 1) // 2
    print(ans)


def enumrate(A):
    dic = defaultdict(int)
    for a in A:
        key = a % 100
        dic[key] += 1
    return dic


solve()
