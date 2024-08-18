# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, S = arrange()
    act(N, S)


def arrange():
    N = int(input())
    S = input()
    return N, S


def act(N, S):
    # <の方向から考える
    grass1 = [1] * N
    streak1 = 1
    for i in range(N-1):
        s = S[i]
        if s == "A":
            streak1 += 1
        else:
            streak1 = 1
        grass1[i+1] = streak1
    # >の方向を逆から考える
    grass2 = [1] * N
    streak2 = 1
    for j in reversed(range(N-1)):
        s = S[j]
        if s == "A":
            streak2 = 1
        else:
            streak2 += 1
        grass2[j] = streak2
    # あとはそれぞれの大きい方が草の最小値となる
    ans = 0
    for i in range(N):
        ans += max(grass1[i], grass2[i])
    print(ans)


solve()
