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


def act(N,  S):
    # 最後の手から考える
    # 最後に3色連続している部分があれば絶対に達成できる
    for i in range(N-2):
        s1 = S[i]
        s2 = S[i+1]
        s3 = S[i+2]
        if s1 == s2 and s2 == s3:
            print("Yes")
            exit()
    print("No")


solve()
